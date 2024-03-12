import time

from MDGLogic.AbstractMDGThread import AbstractMDGThread


class CriticalMBThread(AbstractMDGThread):
    def __init__(self, title: str, text: str) -> None:
        self.title = title
        self.text = text
        super().__init__(None)

    def run(self) -> None:
        time.sleep(0.1)
        self.critical_signal.emit(self.title, self.text)
