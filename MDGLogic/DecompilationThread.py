import json
import os.path
import subprocess
import threading
import time
import zipfile
from pathlib import Path

from MDGLogic.AbstractDeobfDecompThread import AbstractDeobfDecompThread
from MDGUtil import PathUtils, FileUtils
from MDGUtil.SubprocessKiller import kill_subprocess


class DecompilationThread(AbstractDeobfDecompThread):
    cache_lock = threading.Lock()

    def run(self) -> None:
        decomp_cmd = self.serialized_widgets['decomp_cmd_line_edit']['text']
        result_folder = os.path.join(PathUtils.DECOMPILED_MODS_PATH,
                                     os.path.basename(self.mod_path.removesuffix('.jar')))
        FileUtils.create_folder(result_folder)

        java_home = self.serialized_widgets['decompiler_java_home_line_edit']['text']
        decomp_cmd_formatted = (PathUtils.format_decompiler_command(decomp_cmd,
                                                                    java_home,
                                                                    PathUtils.TEST_MOD_PATH,
                                                                    PathUtils.TMP_DECOMPILER_TEST_PATH))
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
                cache_path = os.path.join(PathUtils.DECOMPILED_MODS_PATH, 'cache.json')
                with open(cache_path, 'r') as f:
                    cache = json.loads(f.read())
                cache.append(os.path.basename(result_folder))
                with open(cache_path, 'w') as f:
                    f.write(json.dumps(cache))
