import time

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox, QWidget

from MDGLogic.AbstractMDGThread import AbstractMDGThread


class CriticalMBThread(AbstractMDGThread):
    def run(self):
        time.sleep(0.1)
