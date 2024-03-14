import logging
from typing import Any

from PySide6.QtCore import QThread, Signal


class AbstractMDGThread(QThread):
    progress = Signal(int, str)
    critical_signal = Signal(str, str)
    progress_bar = Signal(int)

    def __init__(self, serialized_widgets: dict[str, dict[str, Any] | list[str]]) -> None:
        super().__init__()
        self.serialized_widgets = serialized_widgets
        self.setTerminationEnabled(True)
        logging.info(f'Started {self.__class__.__name__}.')
        self.finished.connect(self.finished_signal)

    def finished_signal(self) -> None:
        logging.info(f'Finished {self.__class__.__name__}.')
