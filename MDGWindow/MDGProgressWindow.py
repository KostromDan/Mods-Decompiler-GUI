# This Python file uses the following encoding: utf-8
import time

from PySide6.QtWidgets import QMainWindow

from MDGLogic.InitThread import InitThread
from MDGui.Ui_MDGProgressWindow import Ui_MDGProgressWindow


class MDGProgressWindow(QMainWindow):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.init_thread = None
        self.ui = Ui_MDGProgressWindow()
        self.ui.setupUi(self)

        self.main_windows = main_window

        self.current_progress_bar = self.ui.init_progress_bar

    def start(self):
        self.init_thread = InitThread()
        self.init_thread.start()
        self.init_thread.progress.connect(self.set_progress)
        self.init_thread.finished.connect(self.copy_mods)

    def copy_mods(self):
        print(1)

    def set_progress(self, value, text):
        self.current_progress_bar.setValue(value)
        self.ui.currently_label.setText(text)
