import logging
import os
import shutil
import time

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGLogic.DeobfuscationThread import DeobfuscationThread
from MDGUtil import PathUtils
from MDGUtil.FileUtils import create_folder


class FailLogic:
    INTERRUPT = 1
    SKIP = 2
    DECOMPILE = 3


def clear_gradle():
    try:
        for folder in os.listdir(PathUtils.FORGE_GRADLE_DEOBF_CACHE_FOLDER):
            if folder.startswith('local_MDG_'):
                shutil.rmtree(os.path.join(PathUtils.FORGE_GRADLE_DEOBF_CACHE_FOLDER, folder))
    except FileNotFoundError:
        logging.warning(f'Could not find {PathUtils.FORGE_GRADLE_DEOBF_CACHE_FOLDER}. Skipping clearing gradle cache.')


class DeobfuscationMainThread(AbstractMDGThread):
    failed_mod_signal = Signal(str)
    fail_logic_signal = Signal(object)

    def __init__(self, widgets):
        super().__init__(widgets)
        self.deobf_threads: list[DeobfuscationThread] = []

    def run(self):
        if not self.serialized_widgets['deobf_check_box']['isChecked']:
            self.progress.emit(100, 'Deobfuscation skipped.')
            logging.info('Deobfuscation skipped.')
            return

        self.progress.emit(0, 'Deobfuscation started.')
        logging.info('Deobfuscation started.')

        allocated_threads_count = self.serialized_widgets['deobf_threads_horizontal_slider']['value']
        deofb_fail_logic = None
        if self.serialized_widgets['deobf_failed_radio_interrupt']['isChecked']:
            deofb_fail_logic = FailLogic.INTERRUPT
        elif self.serialized_widgets['deobf_failed_radio_skip']['isChecked']:
            deofb_fail_logic = FailLogic.SKIP
        elif self.serialized_widgets['deobf_failed_radio_decompile']['isChecked']:
            deofb_fail_logic = FailLogic.DECOMPILE

        self.fail_logic_signal.emit(deofb_fail_logic)

        mods_list = os.listdir(PathUtils.TMP_MODS_PATH)
        mods_iter = iter(mods_list)
        mods_to_deobf_count = len(mods_list)
        processed_mods_count = 0
        started_mods_count = 0

        clear_gradle()
        create_folder(PathUtils.TMP_DEOBFUSCATION_MDKS_PATH)
        create_folder(PathUtils.DEOBFUSCATED_MODS_PATH)

        while processed_mods_count < mods_to_deobf_count:
            if len(self.deobf_threads) < allocated_threads_count and started_mods_count < mods_to_deobf_count:
                mod_name = mods_iter.__next__()
                logging.info(f'Started deobfuscation of {mod_name}')
                deobf_thread = DeobfuscationThread(os.path.join(PathUtils.TMP_MODS_PATH, mod_name),
                                                   started_mods_count, self.serialized_widgets)
                started_mods_count += 1
                self.deobf_threads.append(deobf_thread)
                deobf_thread.start()

            new_threads = []
            for thread in self.deobf_threads:
                if thread.is_alive():
                    new_threads.append(thread)
                else:
                    processed_mods_count += 1
                    self.progress_bar.emit((processed_mods_count / mods_to_deobf_count) * 100)

                    if thread.success:
                        logging.info(f'Finished deobfuscation of {os.path.basename(thread.mod_path)} with success.')
                        os.remove(thread.mod_path)
                    else:
                        match deofb_fail_logic:
                            case FailLogic.SKIP:
                                logging.warning(
                                    f'Finished deobfuscation of {os.path.basename(thread.mod_path)} with error. Mod will be skipped.')
                                os.remove(thread.mod_path)

                            case FailLogic.DECOMPILE:
                                logging.warning(
                                    f'Finished deobfuscation of {os.path.basename(thread.mod_path)} with error. Mod will be decompiled without deofuscation.')

                            case FailLogic.INTERRUPT:
                                logging.critical(
                                    f'Finished deobfuscation of {os.path.basename(thread.mod_path)} with error. Interrupted.')
                                self.critical_signal.emit('Deobfuscation failed',
                                                          f'Deobfuscation of {os.path.basename(thread.mod_path)} failed!')
                        self.failed_mod_signal.emit(os.path.basename(thread.mod_path))

            self.deobf_threads = new_threads
            time.sleep(0.1)

        logging.info('Deobfuscation complete.')

        self.progress.emit(100, 'Deobfuscation complete.')

        shutil.rmtree(PathUtils.TMP_DEOBFUSCATION_MDKS_PATH)

        clear_gradle()

        if not self.serialized_widgets['merge_check_box']['isEnabled'] or not \
                self.serialized_widgets['merge_check_box']['isChecked']:
            shutil.rmtree(PathUtils.MERGED_MDK_PATH)

    def terminate(self):
        for thread in self.deobf_threads:
            thread.terminate()
        super().terminate()
