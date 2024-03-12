import json
import logging
import os
import time
from typing import Iterator

from MDGLogic.AbstractDeobfDecompMainThread import AbstractDeobfDecompMainThread
from MDGLogic.DecompilationThread import DecompilationThread
from MDGUtil import PathUtils
from MDGUtil.FileUtils import create_folder


def get_mods_iter(use_cached: list) -> Iterator[os.PathLike]:
    try:
        for mod in os.listdir(PathUtils.TMP_MODS_PATH):
            yield os.path.join(PathUtils.TMP_MODS_PATH, mod)
    except FileNotFoundError:
        pass
    try:
        for mod in os.listdir(PathUtils.DEOBFUSCATED_MODS_PATH):
            if mod.removesuffix('_mapped_official.jar') + '.jar' not in use_cached:
                yield os.path.join(PathUtils.DEOBFUSCATED_MODS_PATH, mod)
    except FileNotFoundError:
        pass


class DecompilationMainThread(AbstractDeobfDecompMainThread):
    def run(self) -> None:
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

        create_folder(PathUtils.DECOMPILED_MODS_PATH)

        with open(os.path.join(PathUtils.DECOMPILED_MODS_PATH, 'cache.json'), 'w') as f:
            cache = []
            for mod in os.listdir(PathUtils.DECOMPILED_MODS_PATH):
                if os.path.isdir(os.path.join(PathUtils.DECOMPILED_MODS_PATH, mod)):
                    cache.append(mod)
            f.write(json.dumps(cache))

        while processed_mods_count < mods_to_decomp_count:
            if len(self.threads) < allocated_threads_count and started_mods_count < mods_to_decomp_count:
                mod_path = mods_iter.__next__()
                mod_name = os.path.basename(mod_path)
                logging.info(f'Started decompilation of {mod_name}')
                decomp_thread = DecompilationThread(mod_path,
                                                    started_mods_count, self.serialized_widgets)
                started_mods_count += 1
                self.threads.append(decomp_thread)
                decomp_thread.start()

            new_threads = []
            for thread in self.threads:
                if thread.is_alive():
                    new_threads.append(thread)
                else:
                    processed_mods_count += 1
                    self.progress_bar.emit((processed_mods_count / mods_to_decomp_count) * 100)
                    if thread.success:
                        logging.info(f'Finished decompilation of {os.path.basename(thread.mod_path)} with success.')
                    else:
                        logging.warning(f'Finished decompilation of {os.path.basename(thread.mod_path)} with error.\n'
                                        f"Out directory is empty or doesn't contain a single *.java file")
                        self.failed_mod_signal.emit(os.path.basename(thread.mod_path))

            self.threads = new_threads
            time.sleep(0.1)

        logging.info('Decompilation complete.')

        self.progress.emit(100, 'Decompilation complete.')
