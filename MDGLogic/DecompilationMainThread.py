import json
import logging
import os
import time

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGLogic.DecompilationThread import DecompilationThread
from MDGUtil.FileUtils import create_folder


def get_mods_iter(use_cached):
    try:
        for mod in os.listdir('tmp/mods'):
            yield os.path.join('tmp', 'mods', mod)

        for mod in os.listdir('result/deobfuscated_mods'):
            if mod.removesuffix('_mapped_official.jar')+'.jar' not in use_cached:
                yield os.path.join('result', 'deobfuscated_mods', mod)
    except FileNotFoundError:
        pass


class DecompilationMainThread(AbstractMDGThread):
    failed_mod_signal = Signal(str)

    def __init__(self, widgets):
        super().__init__(widgets)
        self.decomp_threads: list[DecompilationThread] = []

    def run(self):
        if not self.serialized_widgets['decomp_check_box']['isChecked']:
            self.progress.emit(100, 'Decompilation skipped.')
            logging.info('Decompilation skipped.')
            return

        logging.info('Started decompilation.')
        self.progress.emit(0, 'Started decompilation.')

        allocated_threads_count = self.serialized_widgets['decomp_threads_horizontal_slider']['value']

        mods_iter = get_mods_iter(self.serialized_widgets['use_cached'])
        mods_to_decomp_count = len(list(get_mods_iter(self.serialized_widgets['use_cached'])))
        processed_mods_count = 0
        started_mods_count = 0

        create_folder('result/decompiled_mods')

        with open(os.path.join('result', 'decompiled_mods', 'cache.json'), 'w') as f:
            cache = []
            for mod in os.listdir(os.path.join('result', 'decompiled_mods')):
                if os.path.isdir(os.path.join('result', 'decompiled_mods', mod)):
                    cache.append(mod)
            f.write(json.dumps(cache))

        while processed_mods_count < mods_to_decomp_count:
            if len(self.decomp_threads) < allocated_threads_count and started_mods_count < mods_to_decomp_count:
                mod_path = mods_iter.__next__()
                mod_name = os.path.basename(mod_path)
                logging.info(f'Started decompilation of {mod_name}')
                decomp_thread = DecompilationThread(mod_path,
                                                    started_mods_count, self.serialized_widgets)
                started_mods_count += 1
                self.decomp_threads.append(decomp_thread)
                decomp_thread.start()

            new_threads = []
            for thread in self.decomp_threads:
                if thread.is_alive():
                    new_threads.append(thread)
                else:
                    processed_mods_count += 1
                    self.progress_bar.emit((processed_mods_count / mods_to_decomp_count) * 100)
                    if thread.success:
                        logging.info(f'Finished decompilation of {os.path.basename(thread.mod_path)} with success.')
                    else:
                        logging.warning(f'Finished decompilation of {os.path.basename(thread.mod_path)} with error.\n'
                                        f'Out directory is empty or doesn\'t contain a single *.java file')
                        self.failed_mod_signal.emit(os.path.basename(thread.mod_path))


            self.decomp_threads = new_threads
            time.sleep(0.1)

        logging.info('Decompilation complete.')

        self.progress.emit(100, 'Decompilation complete.')

    def terminate(self):
        for thread in self.decomp_threads:
            thread.terminate()
        super().terminate()
