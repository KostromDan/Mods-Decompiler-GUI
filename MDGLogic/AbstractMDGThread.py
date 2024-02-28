from threading import Thread

from PySide6.QtCore import QThread


class AbstractMDGThread(QThread):
    def __init__(self, progress_window):
        super().__init__()
        self.progress_window = progress_window
