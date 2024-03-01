import multiprocessing
import os.path
import shutil
import signal
import subprocess
import time

import psutil

from MDGLogic.MdkInitialisationThread import unzip_and_patch_mdk
from MDGUtil.SubprocessKiller import kill_subprocess


class DeobfuscationThread(multiprocessing.Process):

    def __init__(self, mod_path: str, thread_number: int, serialized_widgets: dict):
        super().__init__()
        self.mod_path = mod_path
        self.thread_number = thread_number
        self.serialized_widgets = serialized_widgets
        self.is_cmd_started = multiprocessing.Value('b', False)
        self.kill_cmd = multiprocessing.Value('b', False)
        self.success = multiprocessing.Value('b', False)

    def run(self):
        current_mdk_path = f'tmp/deobfuscation_MDKs/mdk_{self.thread_number}'
        deobfed_folder_name = f'local_MDG_{self.thread_number}'
        unzip_and_patch_mdk(self.serialized_widgets['mdk_path_line_edit']['text'],
                            current_mdk_path,
                            deobfed_folder_name,
                            True)
        shutil.copy(self.mod_path, os.path.join(current_mdk_path, 'libs'))
        self.cmd = subprocess.Popen(["gradlew.bat", "compileJava"], cwd=current_mdk_path, shell=True)
        with self.is_cmd_started.get_lock():
            self.is_cmd_started.value = True
        while self.cmd.poll() is None:
            time.sleep(0.1)
            if self.kill_cmd.value:
                kill_subprocess(self.cmd.pid)
                return
        deobfed_mods_path = os.path.join(os.path.expanduser('~'),
                                         '.gradle',
                                         'caches',
                                         'forge_gradle',
                                         'deobf_dependencies',
                                         deobfed_folder_name)
        if not os.path.exists(deobfed_mods_path):
            return

        for mod_dir in os.listdir(deobfed_mods_path):
            dir_2 = os.path.join(deobfed_mods_path, mod_dir)
            jar_dir = os.path.join(dir_2, os.listdir(dir_2)[0])
            for file in os.listdir(jar_dir):
                if file.endswith('.jar'):
                    path_to_jar = os.path.join(jar_dir, file)
                    mod_original_name = os.path.basename(self.mod_path)
                    mod_new_mapped_name = mod_original_name.rstrip('.jar') + '_mapped_official.jar'
                    new_jar_path = os.path.join(os.path.dirname(path_to_jar), mod_new_mapped_name)
                    try:
                        os.rename(path_to_jar,
                                  new_jar_path)
                    except FileExistsError:
                        pass
                    shutil.copy(new_jar_path, 'result/deobfuscated_mods')
                    break
        with self.success.get_lock():
            self.success.value = True

    def is_success(self):
        return self.success.value

    def terminate(self):
        with self.kill_cmd.get_lock():
            self.kill_cmd.value = True
        if not self.is_cmd_started.value:
            try:
                super().kill()
            except AttributeError:
                pass
