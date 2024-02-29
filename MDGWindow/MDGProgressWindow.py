# This Python file uses the following encoding: utf-8
import logging

from PySide6.QtGui import QTextCursor, QColor
from PySide6.QtWidgets import QMainWindow, QMessageBox

from MDGLogic.InitThread import InitThread
from MDGUtil.MDGLogger import MDGLogger
from MDGui.Ui_MDGProgressWindow import Ui_MDGProgressWindow


class MDGProgressWindow(QMainWindow):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.ui = Ui_MDGProgressWindow()
        self.ui.setupUi(self)

        self.main_window = main_window

        self.thread_list = []
        self.current_progress_bar = self.ui.init_progress_bar

        self.ui.stop_button.clicked.connect(self.stop_button)

        MDGLogger().pyside_logger_function = self.append_logger
        logging.info("Progress window started.")

    def destroy(self, destroyWindow=..., destroySubWindows=...):
        if len(self.thread_list) >= 1:
            logging.info("Killing threads.")

            for thread in self.thread_list:
                thread.stop()
            self.thread_list.clear()
            logging.info("Killed threads.")
        MDGLogger().pyside_logger_function = None
        logging.info("MDGProgressWindow finished.")
        super().destroy()

    def stop_button(self):
        self.main_window.setEnabled(True)
        self.main_window.show()
        self.destroy()

    def start(self):
        init_thread = InitThread(self.main_window.ui.decomp_cmd_line_edit.text())
        self.thread_list.append(init_thread)
        init_thread.start()
        init_thread.progress.connect(self.set_progress)
        init_thread.decomp_cmd_check_failed.connect(self.decomp_cmd_check_failed)
        init_thread.finished.connect(self.copy_mods)

    def copy_mods(self):
        pass

    def set_progress(self, value, text):
        self.current_progress_bar.setValue(value)
        self.ui.currently_label.setText(text)

    def decomp_cmd_check_failed(self):
        self.main_window.setEnabled(True)
        self.main_window.show()
        self.main_window.ui.decomp_cmd_line_edit.setStyleSheet("border: 1px solid red")
        QMessageBox.critical(self, 'Incorrect decompiler cmd',
                             f"With this decompiler/decompiler cmd program won't work.\n"
                             "This message indicates that {path_to_jar} is not decompiled to {out_path}.\n"
                             f'Check decompiler/decompiler cmd: path, syntax, etc. And try again.',
                             QMessageBox.StandardButton.Ok)
        self.destroy()

    def append_logger(self, color, msg):
        cursor = self.ui.logger_text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.movePosition(QTextCursor.End)

        line_format = cursor.charFormat()
        line_format.setForeground(QColor(color))
        cursor.setCharFormat(line_format)

        cursor.insertText(msg)
        cursor.insertText("\n")
