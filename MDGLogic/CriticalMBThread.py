import time

from MDGLogic.AbstractMDGThread import AbstractMDGThread


class CriticalMBThread(AbstractMDGThread):
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        super().__init__(None)

    def run(self):
        time.sleep(0.1)
        self.critical_signal.emit(self.s1, self.s2)
