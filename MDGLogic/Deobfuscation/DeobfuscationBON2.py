import os
import subprocess
import threading
from multiprocessing.managers import ValueProxy

from MDGLogic.Deobfuscation.DeobfuscatioUtils import Status
from MDGUtil import PathUtils, FileUtils
from MDGUtil.SubprocessOutsAnalyseThread import SubprocessOutsAnalyseThread


def deobfuscate_bon2(mod_path: str | os.PathLike,
                     out_path: str | os.PathLike,
                     java_home: str | os.PathLike,
                     bon2_cmd: str,
                     bon2_version: str,
                     bon2_mappings: str,
                     thread_number: int,
                     lock: threading.Lock,
                     status: ValueProxy[int],
                     stdout: ValueProxy[str],
                     stderr: ValueProxy[str],
                     stdall: ValueProxy[str],
                     cmd_pid: ValueProxy[int]) -> None:
    with lock:
        status.value = Status.STARTED
    mod_original_name = os.path.basename(mod_path)
    mod_new_mapped_name = mod_original_name.removesuffix('.jar') + '_mapped.jar'
    out_path_with_file_name = os.path.join(out_path, mod_new_mapped_name)
    bon2_cmd_formatted = PathUtils.format_bon2_command(bon2_cmd,
                                                       java_home,
                                                       mod_path,
                                                       out_path_with_file_name,
                                                       bon2_version,
                                                       bon2_mappings)

    with lock:
        cmd = subprocess.Popen(bon2_cmd_formatted, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               shell=True)
        analyse_thread = SubprocessOutsAnalyseThread(cmd,repeat_output_to_sys_out=True)
        analyse_thread.start()
        cmd_pid.value = cmd.pid
    analyse_thread.join()
    with lock:
        stdout.value = analyse_thread.out
        stderr.value = analyse_thread.err
        stdall.value = analyse_thread.all
    if analyse_thread.err != '':
        print(mod_original_name, analyse_thread.err)
        try:
            os.remove(out_path_with_file_name)
        except FileNotFoundError:
            pass

    if not os.path.exists(out_path_with_file_name):
        return

    with lock:
        status.value = Status.SUCCESS
        FileUtils.append_cache(PathUtils.DEOBFUSCATED_CACHE_PATH,
                               mod_original_name,
                               FileUtils.get_original_mod_hash(mod_original_name))
