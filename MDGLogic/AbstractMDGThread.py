from PySide6.QtCore import QThread, Signal


class AbstractMDGThread(QThread):
    progress = Signal(int, str)

    def __init__(self):
        super().__init__()
        self.setTerminationEnabled(True)

    def stop(self):
        self.terminate()