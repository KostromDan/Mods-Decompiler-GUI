import logging
import multiprocessing
import os
import time
from pathlib import Path
from typing import Iterator, Any

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGLogic.Decompilation.DecompilationThread import decompile
from MDGLogic.Deobfuscation.DeobfuscatioUtils import Status
from MDGLogic.InitialisationThread import ExceptionThread
from MDGUtil import PathUtils, FileUtils
from MDGUtil.SubprocessKiller import kill_subprocess


def get_mods_iter(use_cached: list) -> Iterator[os.PathLike]:
    if os.path.exists(PathUtils.TMP_MODS_PATH):
        for mod in os.listdir(PathUtils.TMP_MODS_PATH):
            yield os.path.join(PathUtils.TMP_MODS_PATH, mod)
    if os.path.exists(PathUtils.DEOBFUSCATED_MODS_PATH):
        for mod in os.listdir(PathUtils.DEOBFUSCATED_MODS_PATH):
            if mod.removesuffix('_mapped.jar') + '.jar' not in use_cached and not mod.endswith('.json'):
                yield os.path.join(PathUtils.DEOBFUSCATED_MODS_PATH, mod)


class DecompilationThread(AbstractMDGThread):
    failed_mod_signal = Signal(str)

    def __init__(self, widgets: dict[str, dict[str, Any] | list[str]]) -> None:
        super().__init__(widgets)
        self.threads_data: dict[int, dict[str, Any]] = dict()
        self.lock: multiprocessing.Lock = None
        self.finished_mods_count = 0
        self.started_mods_count = 0
        self.mods_list = list(get_mods_iter(self.serialized_widgets['use_cached']))
        self.mods_to_decomp_count = len(list(self.mods_list))
        self.started_mods_set = set()
        self.terminated = 0

    def terminate(self) -> None:
        self.terminated = 1
        while not self.isFinished() and self.terminated != 2:
            time.sleep(0.1)

    def decomp_callback(self, thread_number: int, exception: Exception = None) -> None:
        self.finished_mods_count += 1
        self.progress_bar.emit((self.finished_mods_count / self.mods_to_decomp_count) * 100)

        if exception:
            thread = ExceptionThread(exception)
            thread.start()
            thread.wait()

        with self.lock:
            thread_data = self.threads_data[thread_number]
            mod_path = thread_data['mod_path']
            mod_name = os.path.basename(mod_path)

            if thread_data['stdall'].value != '':
                logging_func = lambda e: logging.warning(e, extra={
                    'debug': not self.serialized_widgets['decomp_logging_warnings_check_box']['isChecked']})
                if 'ERROR: ' in thread_data['stdall'].value:
                    logging_func = lambda e: logging.error(e, extra={
                        'debug': not self.serialized_widgets['decomp_logging_errors_check_box']['isChecked']})
                logging_func(f'Something happened while decompiling {mod_name}. stdout & stderr:\n'
                             f"{thread_data['stdall'].value}")

            match thread_data['status'].value:
                case Status.SUCCESS:
                    logging.info(f'Finished decompilation of {mod_name} with success.')
                case _:
                    thread_data['status'].value = Status.FAILED

                    if not list(Path(thread_data['out_path']).rglob('*.java')):
                        logging.warning(f'Finished decompilation of {mod_name} with error.\n'
                                        f"Out directory doesn't contain a single *.java file")
                    else:
                        logging.warning(f'Finished decompilation of {mod_name} with error.')
                    self.failed_mod_signal.emit(mod_name)

    def run(self) -> None:
        if not self.serialized_widgets['decomp_check_box']['isChecked']:
            self.progress.emit(100, 'Decompilation skipped.')
            logging.info('Decompilation skipped.')
            return

        logging.info('Started decompilation.')
        self.progress.emit(0, 'Started decompilation.')

        allocated_threads_count = self.serialized_widgets['decomp_threads_horizontal_slider']['value']

        FileUtils.create_folder(PathUtils.DECOMPILED_MODS_PATH)

        try:
            os.remove(PathUtils.DECOMPILED_CACHE_PATH)
        except FileNotFoundError:
            pass
        for mod in os.listdir(PathUtils.DECOMPILED_MODS_PATH):
            if os.path.isdir(os.path.join(PathUtils.DECOMPILED_MODS_PATH, mod)):
                FileUtils.append_cache(PathUtils.DECOMPILED_CACHE_PATH, mod, FileUtils.get_original_mod_hash(mod))

        with multiprocessing.Manager() as manager:
            self.lock = manager.Lock()
            with multiprocessing.Pool(processes=allocated_threads_count) as pool:
                with self.lock:
                    for thread_number, mod_path in enumerate(self.mods_list):
                        mod_name = os.path.basename(mod_path).removesuffix('.jar')
                        self.threads_data[thread_number] = {
                            'mod_path': mod_path,
                            'out_path': os.path.join(PathUtils.DECOMPILED_MODS_PATH, mod_name),
                            'decomp_cmd': self.serialized_widgets['decomp_cmd_line_edit']['text'],
                            'java_home': self.serialized_widgets['decompiler_java_home_line_edit']['text'],
                            'thread_number': thread_number,
                            'lock': self.lock,
                            'status': manager.Value(int, Status.CREATED),
                            'stdout': manager.Value(str, ''),
                            'stderr': manager.Value(str, ''),
                            'stdall': manager.Value(str, ''),
                            'cmd_pid': manager.Value(int, -1)}
                        pool.apply_async(decompile,
                                         kwds=self.threads_data[thread_number],
                                         callback=lambda x, n=thread_number: self.decomp_callback(n),
                                         error_callback=lambda e, n=thread_number: self.decomp_callback(n, exception=e))
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
                            logging.info(f"Started decompilation of {os.path.basename(thread_data['mod_path'])}")
                    time.sleep(0.1)

                pool.join()

        logging.info('Decompilation complete.')

        self.progress.emit(100, 'Decompilation complete.')