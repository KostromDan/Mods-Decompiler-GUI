# This Python file uses the following encoding: utf-8
import sys
import time
from threading import Thread

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QApplication, QMainWindow

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
        self.init_thread = InitThread(self)
        self.init_thread.start()

    def set_progress(self, value, text):
        self.current_progress_bar.setValue(value)
        self.ui.currently_label.setText(text)
