import logging
from collections import defaultdict

from PySide6.QtCore import QThread, Signal


class AbstractMDGThread(QThread):
    progress = Signal(int, str)
    critical_signal = Signal(str, str)
    progress_bar = Signal(int)

    def __init__(self, serialized_widgets):
        super().__init__()
        self.setTerminationEnabled(True)
        logging.info(f'Started {self.__class__.__name__}.')
        self.finished.connect(self.finished_signal)
        self.serialized_widgets: defaultdict[dict] = serialized_widgets

    def finished_signal(self):
        logging.info(f'Finished {self.__class__.__name__}.')
