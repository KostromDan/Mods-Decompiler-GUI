import subprocess
import threading
from typing import Optional, Union, Any


def do_nothing(s):
    pass


class AbstractDeobfDecompThread(threading.Thread):
    def __init__(self,
                 mod_path: str,
                 thread_number: int,
                 serialized_widgets: dict[str, Union[dict[str, Any], list[str]]]) -> None:
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
