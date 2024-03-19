from typing import Optional, Any

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGLogic.DecompilationThread import DecompilationThread


class AbstractDeobfDecompMainThread(AbstractMDGThread):
    failed_mod_signal = Signal(str)

    def __init__(self, widgets: dict[str, dict[str, Any] | list[str]]) -> None:
        super().__init__(widgets)
        self.threads: list[Optional[DecompilationThread]] = []

    def terminate(self) -> None:
        for thread in self.threads:
            thread.terminate()
        super().terminate()
