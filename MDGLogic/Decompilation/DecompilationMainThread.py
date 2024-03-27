import logging
import os
import time
from typing import Iterator, Any, Optional

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGLogic.Decompilation.DecompilationThread import DecompilationThread
from MDGUtil import PathUtils, FileUtils


def get_mods_iter(use_cached: list) -> Iterator[os.PathLike]:
    if os.path.exists(PathUtils.TMP_MODS_PATH):
        for mod in os.listdir(PathUtils.TMP_MODS_PATH):
            yield os.path.join(PathUtils.TMP_MODS_PATH, mod)
    if os.path.exists(PathUtils.DEOBFUSCATED_MODS_PATH):
        for mod in os.listdir(PathUtils.DEOBFUSCATED_MODS_PATH):
            if mod.removesuffix('_mapped.jar') + '.jar' not in use_cached and not mod.endswith('.json'):
                yield os.path.join(PathUtils.DEOBFUSCATED_MODS_PATH, mod)


class DecompilationMainThread(AbstractMDGThread):
    failed_mod_signal = Signal(str)

    def __init__(self, widgets: dict[str, dict[str, Any] | list[str]]) -> None:
        super().__init__(widgets)
        self.threads: list[Optional[DecompilationThread]] = []

    def terminate(self) -> None:
        for thread in self.threads:
            thread.terminate()
        super().terminate()

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

        FileUtils.create_folder(PathUtils.DECOMPILED_MODS_PATH)

        try:
            os.remove(PathUtils.DECOMPILED_CACHE_PATH)
        except FileNotFoundError:
            pass
        for mod in os.listdir(PathUtils.DECOMPILED_MODS_PATH):
            if os.path.isdir(os.path.join(PathUtils.DECOMPILED_MODS_PATH, mod)):
                FileUtils.append_cache(PathUtils.DECOMPILED_CACHE_PATH, mod, FileUtils.get_original_mod_hash(mod))

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
