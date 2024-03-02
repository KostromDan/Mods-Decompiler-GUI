import multiprocessing
import os.path
import shutil
import subprocess
import time
from pathlib import Path

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
        deobfed_mods_path = os.path.join(os.path.expanduser('~'),
                                         '.gradle',
                                         'caches',
                                         'forge_gradle',
                                         'deobf_dependencies',
                                         deobfed_folder_name)
        self.cmd = subprocess.Popen(["gradlew.bat", "compileJava"], cwd=current_mdk_path, shell=True)
        with self.is_cmd_started.get_lock():
            self.is_cmd_started.value = True
        while self.cmd.poll() is None:
            time.sleep(0.1)
            path_to_jar_list = list(Path(deobfed_mods_path).rglob('*.jar'))
            if path_to_jar_list:
                path_to_jar = os.path.join(path_to_jar_list[0])
                cur_size = os.path.getsize(path_to_jar)
                old_size = -1
                while cur_size == 0 or cur_size > old_size:
                    old_size = cur_size
                    cur_size = os.path.getsize(path_to_jar)
                    time.sleep(0.1)
                # time_fisihed=datetime.datetime.now()
                # while self.cmd.poll() is None:
                #     pass
                # print(f'Time saved: {datetime.datetime.now()-time_fisihed}.')

            if path_to_jar_list or self.kill_cmd.value:
                kill_subprocess(self.cmd.pid)

            if self.kill_cmd.value:
                return

        if not path_to_jar_list:
            return

        mod_original_name = os.path.basename(self.mod_path)
        mod_new_mapped_name = mod_original_name.rstrip('.jar') + '_mapped_official.jar'
        new_jar_path = os.path.join(os.path.dirname(path_to_jar), mod_new_mapped_name)
        try:
            os.rename(path_to_jar,
                      new_jar_path)
        except FileExistsError:
            pass
        shutil.copy(new_jar_path, 'result/deobfuscated_mods')
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
