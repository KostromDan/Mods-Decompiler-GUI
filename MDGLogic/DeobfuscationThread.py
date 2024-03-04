import os.path
import shutil
import subprocess
import threading
import time
from pathlib import Path

from MDGLogic.MdkInitialisationThread import unzip_and_patch_mdk
from MDGUtil.SubprocessKiller import kill_subprocess


def remove_unsupported_symbols(mod_name):
    new_name = []
    for symbol in mod_name:
        if symbol.isalpha() or symbol.isdigit() or symbol in ['-', '.']:
            new_name.append(symbol)
            continue
        new_name.append('-')
    if new_name[-1] == '-':
        new_name.append('mod')
    return ''.join(new_name)


class DeobfuscationThread(threading.Thread):

    def __init__(self, mod_path: str, thread_number: int, serialized_widgets: dict):
        super().__init__()
        self.mod_path = mod_path
        self.thread_number = thread_number
        self.serialized_widgets = serialized_widgets
        self.is_cmd_started = False
        self.kill_cmd = False
        self.success = False

    def run(self):
        current_mdk_path = f'tmp/deobfuscation_MDKs/mdk_{self.thread_number}'
        deobfed_folder_name = f'local_MDG_{self.thread_number}'
        unzip_and_patch_mdk(self.serialized_widgets['mdk_path_line_edit']['text'],
                            current_mdk_path,
                            deobfed_folder_name,
                            True)
        shutil.copy(self.mod_path, os.path.join(current_mdk_path, 'libs'))
        new_mod_name = remove_unsupported_symbols(os.path.basename(self.mod_path))
        os.rename(os.path.join(current_mdk_path, 'libs', os.path.basename(self.mod_path)),
                  os.path.join(current_mdk_path, 'libs', new_mod_name))
        deobfed_mods_path = os.path.join(os.path.expanduser('~'),
                                         '.gradle',
                                         'caches',
                                         'forge_gradle',
                                         'deobf_dependencies',
                                         deobfed_folder_name)
        self.cmd = subprocess.Popen(['gradlew.bat', 'compileJava'], cwd=current_mdk_path, shell=True)
        self.is_cmd_started = True
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

            if path_to_jar_list or self.kill_cmd:
                kill_subprocess(self.cmd.pid)

            if self.kill_cmd:
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
        self.success = True

    def is_success(self):
        return self.success

    def terminate(self):
        self.kill_cmd = True
        if not self.is_cmd_started:
            try:
                super().kill()
            except AttributeError:
                pass
