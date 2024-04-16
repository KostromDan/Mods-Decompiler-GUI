import os.path
import subprocess
import threading
import zipfile
from multiprocessing.managers import ValueProxy, ListProxy
from pathlib import Path

from MDGLogic.Deobfuscation.DeobfuscatioUtils import Status
from MDGUtil import PathUtils, FileUtils
from MDGUtil.SubprocessOutsAnalyseThread import SubprocessOutsAnalyseThread


def decompile(mod_path: str | os.PathLike,
              out_path: str | os.PathLike,
              decomp_cmd: str,
              java_home: str | os.PathLike,
              thread_number: int,
              lock: threading.Lock,
              status: ValueProxy[int],
              stdall: ValueProxy[str],
              formatted_cmd: ValueProxy[str],
              all_msgs: ListProxy,
              cmd_pid: ValueProxy[int]) -> None:
    with lock:
        status.value = Status.STARTED
    mod_name = os.path.basename(mod_path)
    FileUtils.create_folder(out_path)

    with lock:
        decomp_cmd_formatted = (PathUtils.format_decompiler_command(decomp_cmd,
                                                                    java_home,
                                                                    mod_path,
                                                                    out_path))
        formatted_cmd.value = decomp_cmd_formatted
        cmd = subprocess.Popen(decomp_cmd_formatted, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        analyse_thread = SubprocessOutsAnalyseThread(cmd)
        analyse_thread.start()
        cmd_pid.value = cmd.pid
    analyse_thread.join()
    with lock:
        stdall.value = analyse_thread.all
        all_msgs.extend(analyse_thread.all_msgs)
    try:
        decompiled_jar_path = os.path.join(out_path, os.path.basename(mod_path))
        zipfile.ZipFile(decompiled_jar_path).extractall(out_path)
        os.remove(decompiled_jar_path)
    except FileNotFoundError:
        pass
    if list(Path(out_path).rglob('*.java')):
        with lock:
            status.value = Status.SUCCESS
            FileUtils.append_cache(PathUtils.DECOMPILED_CACHE_PATH,
                                   mod_name,
                                   FileUtils.get_original_mod_hash(mod_name))
