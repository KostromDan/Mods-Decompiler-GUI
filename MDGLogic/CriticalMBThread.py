import time

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread


class CriticalMBThread(AbstractMDGThread):
    str_signal = Signal(str)

    def __init__(self, msg):
        self.msg = msg
        super().__init__(None)

    def run(self):
        time.sleep(0.1)
        self.str_signal.emit(self.msg)
