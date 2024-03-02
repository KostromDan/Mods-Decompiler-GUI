import multiprocessing
import os.path
import subprocess
import time
import zipfile

from MDGUtil.FileUtils import create_folder
from MDGUtil.SubprocessKiller import kill_subprocess


class DecompilationThread(multiprocessing.Process):

    def __init__(self, mod_path: str, thread_number: int, serialized_widgets: dict):
        super().__init__()
        self.mod_path = mod_path
        self.thread_number = thread_number
        self.serialized_widgets = serialized_widgets
        self.is_cmd_started = multiprocessing.Value('b', False)
        self.kill_cmd = multiprocessing.Value('b', False)

    def run(self):
        decomp_cmd = self.serialized_widgets['decomp_cmd_line_edit']['text']
        result_folder = os.path.join('result', 'decompiled_mods', os.path.basename(self.mod_path.rstrip('.jar')))
        create_folder(result_folder)
        decomp_cmd_formatted = decomp_cmd.format(path_to_jar=self.mod_path, out_path=result_folder)
        self.cmd = subprocess.Popen(decomp_cmd_formatted.split(' '), shell=True)
        with self.is_cmd_started.get_lock():
            self.is_cmd_started.value = True
        while self.cmd.poll() is None:
            time.sleep(0.1)
            if self.kill_cmd.value:
                kill_subprocess(self.cmd.pid)
                return
        decompiled_jar_path = os.path.join(result_folder, os.path.basename(self.mod_path))
        zipfile.ZipFile(decompiled_jar_path).extractall(result_folder)
        os.remove(decompiled_jar_path)

    def terminate(self):
        with self.kill_cmd.get_lock():
            self.kill_cmd.value = True
        if not self.is_cmd_started.value:
            try:
                super().kill()
            except AttributeError:
                pass
