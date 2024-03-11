import os.path
import shutil
import subprocess
import threading
import time
from pathlib import Path

from MDGLogic.MdkInitialisationThread import unzip_and_patch_mdk
from MDGUtil import PathUtils
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
        current_mdk_path = os.path.join(PathUtils.TMP_DEOBFUSCATION_MDKS_PATH, f'mdk_{self.thread_number}')
        folder_name_in_gradle_cache = f'local_MDG_{self.thread_number}'
        unzip_and_patch_mdk(self.serialized_widgets['mdk_path_line_edit']['text'],
                            current_mdk_path,
                            folder_name_in_gradle_cache,
                            True)
        shutil.copy(self.mod_path, os.path.join(current_mdk_path, 'libs'))
        new_mod_name = remove_unsupported_symbols(os.path.basename(self.mod_path))
        try:
            os.rename(os.path.join(current_mdk_path, 'libs', os.path.basename(self.mod_path)),
                      os.path.join(current_mdk_path, 'libs', new_mod_name))
        except FileExistsError:
            pass
        current_mod_deobf_path = os.path.join(PathUtils.FORGE_GRADLE_DEOBF_CACHE_FOLDER,
                                              folder_name_in_gradle_cache)
        self.cmd = subprocess.Popen(['gradlew.bat', 'compileJava'], cwd=current_mdk_path, shell=True)
        self.is_cmd_started = True
        while self.cmd.poll() is None:
            time.sleep(0.1)

            if self.kill_cmd:
                kill_subprocess(self.cmd.pid)
                return

        path_to_jar_list = list(Path(current_mod_deobf_path).rglob('*.jar'))

        if not path_to_jar_list:
            return

        path_to_jar = os.path.join(path_to_jar_list[0])

        mod_original_name = os.path.basename(self.mod_path)
        mod_new_mapped_name = mod_original_name.removesuffix('.jar') + '_mapped_official.jar'
        new_jar_path = os.path.join(os.path.dirname(path_to_jar), mod_new_mapped_name)
        try:
            os.rename(path_to_jar,
                      new_jar_path)
        except FileExistsError:
            pass
        shutil.copy(new_jar_path, PathUtils.DEOBFUSCATED_MODS_PATH)
        self.success = True

    def terminate(self):
        self.kill_cmd = True
        if not self.is_cmd_started:
            try:
                super().kill()
            except AttributeError:
                pass
