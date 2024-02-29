# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QMainWindow, QMessageBox

from MDGLogic.InitThread import InitThread
from MDGui.Ui_MDGProgressWindow import Ui_MDGProgressWindow


class MDGProgressWindow(QMainWindow):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.init_thread = None
        self.ui = Ui_MDGProgressWindow()
        self.ui.setupUi(self)

        self.main_window = main_window

        self.current_progress_bar = self.ui.init_progress_bar

    def start(self):
        self.init_thread = InitThread(self.main_window.ui.decomp_cmd_line_edit.text())
        self.init_thread.start()
        self.init_thread.progress.connect(self.set_progress)
        self.init_thread.decomp_cmd_check_failed.connect(self.decomp_cmd_check_failed)
        self.init_thread.finished.connect(self.copy_mods)

    def copy_mods(self):
        print(1)

    def set_progress(self, value, text):
        self.current_progress_bar.setValue(value)
        self.ui.currently_label.setText(text)

    def decomp_cmd_check_failed(self):
        self.main_window.setEnabled(True)
        self.main_window.show()
        self.main_window.ui.decomp_cmd_line_edit.setStyleSheet("border: 1px solid red")
        QMessageBox.critical(self, 'Incorrect decompiler cmd',
                            f"With this decompiler/decompiler cmd program won't work.\n"
                            f'Check decompiler/decompiler cmd: path, syntax, etc. And try again.',
                            QMessageBox.StandardButton.Ok)
        self.destroy()
