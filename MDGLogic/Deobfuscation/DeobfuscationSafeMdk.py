import os
import shutil
import subprocess
import threading
from multiprocessing.managers import ValueProxy
from pathlib import Path

from MDGLogic.Deobfuscation.DeobfuscatioUtils import Status
from MDGLogic.MdkInitialisationThread import unzip_and_patch_mdk
from MDGUtil import PathUtils, FileUtils


def deobfuscate_safe_mdk(mod_path: str | os.PathLike,
                         mdk_path: str | os.PathLike,
                         out_path: str | os.PathLike,
                         java_home: str | os.PathLike,
                         thread_number: int,
                         lock: threading.Lock,
                         status: ValueProxy[int],
                         cmd_pid: ValueProxy[int]) -> None:
    with lock:
        status.value = Status.STARTED
    mod_original_name = os.path.basename(mod_path)
    current_mdk_path = os.path.join(PathUtils.TMP_DEOBFUSCATION_MDKS_PATH, f'mdk_{thread_number}')
    folder_name_in_gradle_cache = f'local_MDG_{thread_number}'
    unzip_and_patch_mdk(mdk_path,
                        current_mdk_path,
                        folder_name_in_gradle_cache,
                        True)
    shutil.copy(mod_path, os.path.join(current_mdk_path, 'libs'))
    current_mod_deobf_path = os.path.join(PathUtils.FORGE_GRADLE_DEOBF_CACHE_FOLDER,
                                          folder_name_in_gradle_cache)

    with lock:
        cmd = subprocess.Popen(['gradlew.bat', 'compileJava'],
                               env=PathUtils.get_env_with_patched_java_home(java_home),
                               cwd=current_mdk_path,
                               shell=True)
        cmd_pid.value = cmd.pid
    cmd.wait()

    path_to_jar_list = list(Path(current_mod_deobf_path).rglob('*.jar'))

    if not path_to_jar_list:
        return

    path_to_jar = os.path.join(path_to_jar_list[0])

    mod_new_mapped_name = mod_original_name.removesuffix('.jar') + '_mapped.jar'
    new_jar_path = os.path.join(os.path.dirname(path_to_jar), mod_new_mapped_name)
    try:
        os.rename(path_to_jar,
                  new_jar_path)
    except FileExistsError:
        pass
    shutil.copy(new_jar_path, out_path)
    with lock:
        status.value = Status.SUCCESS
        FileUtils.append_cache(PathUtils.DEOBFUSCATED_CACHE_PATH,
                               mod_original_name,
                               FileUtils.get_original_mod_hash(mod_original_name))
