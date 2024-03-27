import os.path
import subprocess
import threading
import time
import zipfile
from pathlib import Path
from typing import Any, Optional

from MDGUtil import PathUtils, FileUtils
from MDGUtil.SubprocessKiller import kill_subprocess


class DecompilationThread(threading.Thread):
    cache_lock = threading.Lock()

    def __init__(self,
                 mod_path: str,
                 thread_number: int,
                 serialized_widgets: dict[str, dict[str, Any] | list[str]]) -> None:
        super().__init__()
        self.mod_path = mod_path
        self.thread_number = thread_number
        self.serialized_widgets = serialized_widgets
        self.cmd: Optional[subprocess.Popen] = None
        self.kill_cmd: bool = False
        self.success: bool = False

    def terminate(self) -> None:
        self.kill_cmd = True
        if self.cmd is None:
            try:
                super().kill()
            except AttributeError:
                pass

    def run(self) -> None:
        decomp_cmd = self.serialized_widgets['decomp_cmd_line_edit']['text']
        mod_name = os.path.basename(self.mod_path)
        result_folder = os.path.join(PathUtils.DECOMPILED_MODS_PATH,
                                     mod_name.removesuffix('.jar'))
        FileUtils.create_folder(result_folder)

        java_home = self.serialized_widgets['decompiler_java_home_line_edit']['text']
        decomp_cmd_formatted = (PathUtils.format_decompiler_command(decomp_cmd,
                                                                    java_home,
                                                                    self.mod_path,
                                                                    result_folder))
        self.cmd = subprocess.Popen(decomp_cmd_formatted, shell=True)
        while self.cmd.poll() is None:
            time.sleep(0.1)
            if self.kill_cmd:
                kill_subprocess(self.cmd.pid)
                return
        try:
            decompiled_jar_path = os.path.join(result_folder, os.path.basename(self.mod_path))
            zipfile.ZipFile(decompiled_jar_path).extractall(result_folder)
            os.remove(decompiled_jar_path)
        except FileNotFoundError:
            pass
        if os.listdir(result_folder) or list(Path(result_folder).rglob('*.java')):
            self.success = True
            with self.cache_lock:
                FileUtils.append_cache(PathUtils.DECOMPILED_CACHE_PATH,
                                       mod_name,
                                       FileUtils.get_original_mod_hash(mod_name))
