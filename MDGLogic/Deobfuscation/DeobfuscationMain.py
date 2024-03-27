import logging
import multiprocessing
import os
import os.path
import shutil
import time
from typing import Any

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGLogic.Deobfuscation.DeobfuscatioUtils import FailLogic, Status, clear_forge_gradle, DeobfuscationAlgorithm
from MDGLogic.Deobfuscation.DeobfuscationBON2 import deobfuscate_bon2
from MDGLogic.Deobfuscation.DeobfuscationSafeMdk import deobfuscate_safe_mdk
from MDGLogic.InitialisationThread import ExceptionThread
from MDGUtil import FileUtils
from MDGUtil import PathUtils
from MDGUtil.SubprocessKiller import kill_subprocess


class DeobfuscationThread(AbstractMDGThread):
    fail_logic_signal = Signal(object)
    failed_mod_signal = Signal(str)

    def __init__(self, widgets: dict[str, dict[str, Any] | list[str]]) -> None:
        super().__init__(widgets)
        self.threads_data: dict[int, dict[str, Any]] = dict()
        self.lock: multiprocessing.Lock = None
        self.finished_mods_count = 0
        self.started_mods_count = 0
        self.mods_list = os.listdir(PathUtils.TMP_MODS_PATH)
        self.mods_to_deobf_count = len(self.mods_list)
        self.started_mods_set = set()
        self.terminated = 0

        self.deofb_fail_logic = None
        if self.serialized_widgets['deobf_failed_radio_interrupt']['isChecked']:
            self.deofb_fail_logic = FailLogic.INTERRUPT
        elif self.serialized_widgets['deobf_failed_radio_skip']['isChecked']:
            self.deofb_fail_logic = FailLogic.SKIP
        elif self.serialized_widgets['deobf_failed_radio_decompile']['isChecked']:
            self.deofb_fail_logic = FailLogic.DECOMPILE

        self.deofb_algo = None
        if self.serialized_widgets['deobf_algo_radio_safe_mdk']['isChecked']:
            self.deofb_algo = DeobfuscationAlgorithm.MDK_SAFE
        elif self.serialized_widgets['deobf_algo_radio_fast_mdk']['isChecked']:
            self.deofb_algo = DeobfuscationAlgorithm.MDK_FAST
        elif self.serialized_widgets['deobf_algo_radio_bon2']['isChecked']:
            self.deofb_algo = DeobfuscationAlgorithm.BON2

    def terminate(self) -> None:
        self.terminated = 1
        while not self.isFinished() and self.terminated != 2:
            time.sleep(0.1)

    def deobf_callback(self, thread_number: int, exception: Exception = None) -> None:
        self.finished_mods_count += 1
        self.progress_bar.emit((self.finished_mods_count / self.mods_to_deobf_count) * 100)

        if exception:
            thread = ExceptionThread(exception)
            thread.start()
            time.sleep(0.1)

        with self.lock:
            thread_data = self.threads_data[thread_number]
            mod_path = thread_data['mod_path']
            mod_name = os.path.basename(mod_path)

            match thread_data['status'].value:
                case Status.SUCCESS:
                    logging.info(f'Finished deobfuscation of {mod_name} with success.')
                    os.remove(mod_path)
                case _:
                    self.threads_data[thread_number]['status'].value = Status.FAILED

                    logging.error(f'Error while deobfuscating {mod_name}. stdout & stderr:\n'
                                  f"{self.threads_data[thread_number]['stdall'].value}")
                    match self.deofb_fail_logic:
                        case FailLogic.SKIP:
                            logging.warning(f'Finished deobfuscation of {mod_name} with error. '
                                            f'Mod will be skipped.')
                            os.remove(mod_path)

                        case FailLogic.DECOMPILE:
                            logging.warning(f'Finished deobfuscation of {mod_name} with error. '
                                            f'Mod will be decompiled without deofuscation.')

                        case FailLogic.INTERRUPT:
                            logging.critical(f'Finished deobfuscation of {mod_name} with error. '
                                             f'Interrupted.')
                            self.critical_signal.emit('Deobfuscation failed',
                                                      f'Deobfuscation of {mod_name} failed!', None)
                    self.failed_mod_signal.emit(mod_name)

    def run(self) -> None:
        self.fail_logic_signal.emit(self.deofb_fail_logic)
        if not self.serialized_widgets['deobf_check_box']['isChecked']:
            self.progress.emit(100, 'Deobfuscation skipped.')
            logging.info('Deobfuscation skipped.')
            return

        self.progress.emit(0, 'Deobfuscation started.')
        logging.info('Deobfuscation started.')

        allocated_threads_count = self.serialized_widgets['deobf_threads_horizontal_slider']['value']

        clear_forge_gradle()
        FileUtils.create_folder(PathUtils.TMP_DEOBFUSCATION_MDKS_PATH)
        FileUtils.create_folder(PathUtils.DEOBFUSCATED_MODS_PATH)

        try:
            os.remove(PathUtils.DEOBFUSCATED_CACHE_PATH)
        except FileNotFoundError:
            pass
        for mod in os.listdir(PathUtils.DEOBFUSCATED_MODS_PATH):
            if not os.path.basename(os.path.join(PathUtils.DEOBFUSCATED_MODS_PATH, mod)).endswith('.json'):
                FileUtils.append_cache(PathUtils.DEOBFUSCATED_CACHE_PATH, mod, FileUtils.get_original_mod_hash(mod))

        with multiprocessing.Manager() as manager:
            self.lock = manager.Lock()
            with multiprocessing.Pool(processes=allocated_threads_count) as pool:
                for thread_number, mod_name in enumerate(self.mods_list):
                    self.threads_data[thread_number] = {
                        'mod_path': os.path.join(PathUtils.TMP_MODS_PATH, mod_name),
                        'out_path': PathUtils.DEOBFUSCATED_MODS_PATH,
                        'thread_number': thread_number,
                        'lock': self.lock,
                        'status': manager.Value(int, Status.CREATED),
                        'stdout': manager.Value(str, ''),
                        'stderr': manager.Value(str, ''),
                        'stdall': manager.Value(str, ''),
                        'cmd_pid': manager.Value(int, -1)}
                    deobf_function = None
                    match self.deofb_algo:
                        case DeobfuscationAlgorithm.MDK_SAFE:
                            deobf_function = deobfuscate_safe_mdk
                            self.threads_data[thread_number]['mdk_path'] = \
                                self.serialized_widgets['mdk_path_line_edit']['text']
                            self.threads_data[thread_number]['java_home'] = \
                                self.serialized_widgets['mdk_java_home_line_edit']['text']
                        case DeobfuscationAlgorithm.MDK_FAST:
                            deobf_function = NotImplemented
                            self.threads_data[thread_number]['mdk_path'] = \
                                self.serialized_widgets['mdk_path_line_edit']['text']
                            self.threads_data[thread_number]['java_home'] = \
                                self.serialized_widgets['mdk_java_home_line_edit']['text']
                        case DeobfuscationAlgorithm.BON2:
                            deobf_function = deobfuscate_bon2
                            self.threads_data[thread_number]['bon2_cmd'] = \
                                self.serialized_widgets['bon2_cmd_line_edit']['text']
                            self.threads_data[thread_number]['bon2_version'] = \
                                self.serialized_widgets['bon2_version_combo_box']['currentText']
                            self.threads_data[thread_number]['bon2_mappings'] = \
                                self.serialized_widgets['bon2_mappings_combo_box']['currentText']
                            self.threads_data[thread_number]['bon2_path'] = \
                                self.serialized_widgets['bon2_path_line_edit']['text']
                            self.threads_data[thread_number]['java_home'] = \
                                self.serialized_widgets['bon2_java_home_line_edit']['text']

                    pool.apply_async(deobf_function,
                                     kwds=self.threads_data[thread_number],
                                     callback=lambda x, n=thread_number: self.deobf_callback(n),
                                     error_callback=lambda e, n=thread_number: self.deobf_callback(n, exception=e))
                pool.close()
                while len(pool._cache):
                    if self.terminated:
                        with self.lock:
                            pool.terminate()
                            for thread_number, thread_data in self.threads_data.items():
                                if thread_data['cmd_pid'].value != -1:
                                    kill_subprocess(thread_data['cmd_pid'].value)
                        pool.join()
                        self.terminated = 2
                        return
                    for thread_number, thread_data in self.threads_data.items():
                        if thread_data['status'].value != Status.CREATED and thread_number not in self.started_mods_set:
                            self.started_mods_set.add(thread_number)
                            logging.info(f"Started deobfuscation of {os.path.basename(thread_data['mod_path'])}")
                    time.sleep(0.1)

                pool.join()

        logging.info('Deobfuscation complete.')

        self.progress.emit(100, 'Deobfuscation complete.')

        shutil.rmtree(PathUtils.TMP_DEOBFUSCATION_MDKS_PATH)

        clear_forge_gradle()

        if not self.serialized_widgets['merge_check_box']['isEnabled'] or not \
                self.serialized_widgets['merge_check_box']['isChecked']:
            FileUtils.remove_folder(PathUtils.MERGED_MDK_PATH)
