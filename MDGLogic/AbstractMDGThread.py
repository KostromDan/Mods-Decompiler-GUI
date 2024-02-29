import logging

from PySide6.QtCore import QThread, Signal


class AbstractMDGThread(QThread):
    progress = Signal(int, str)

    def __init__(self):
        super().__init__()
        self.setTerminationEnabled(True)
        logging.info(f'Started {self.__class__.__name__}.')
        self.finished.connect(self.finished_signal)

    def stop(self):
        self.terminate()

    def finished_signal(self):
        logging.info(f'Finished {self.__class__.__name__}.')
