import time

from MDGLogic.AbstractMDGThread import AbstractMDGThread


class CriticalMBThread(AbstractMDGThread):
    def __init__(self, title: str, text: str, widget_name:str) -> None:
        self.title = title
        self.text = text
        self.widget_name = widget_name
        super().__init__(None)

    def run(self) -> None:
        time.sleep(0.1)
        self.critical_signal.emit(self.title, self.text,self.widget_name)
