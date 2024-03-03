# This Python file uses the following encoding: utf-8
import copy
import logging

from PySide6.QtGui import QTextCursor, QColor
from PySide6.QtWidgets import QMainWindow, QMessageBox

from MDGLogic.CopyThread import CopyThread
from MDGLogic.CriticalMBThread import CriticalMBThread
from MDGLogic.DecompilationMainThread import DecompilationMainThread
from MDGLogic.DeobfuscationMainThread import DeobfuscationMainThread
from MDGLogic.InitialisationThread import InitialisationThread
from MDGLogic.MdkInitialisationThread import MdkInitialisationThread
from MDGLogic.MergingThread import MergingThread
from MDGUtil.MDGLogger import MDGLogger
from MDGui.Ui_MDGProgressWindow import Ui_MDGProgressWindow


def only_if_window_active(func):
    def wrapper(self, *args, **kwargs):
        if self.isEnabled():
            result = func(self, *args, **kwargs)
            return result

    return wrapper


class MDGProgressWindow(QMainWindow):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.ui = Ui_MDGProgressWindow()
        self.ui.setupUi(self)

        self.main_window = main_window

        self.thread_list = []
        self.current_progress_bar = self.ui.init_progress_bar

        self.ui.stop_button.clicked.connect(self.stop_button)

        MDGLogger().logger_signal.append_logger_signal.connect(self.append_logger)

        self.completed = False

        logging.info('Progress window started.')

    def destroy(self):
        self.setEnabled(False)
        if len(self.thread_list) >= 1:
            logging.info('Killing threads.')
            for thread in reversed(self.thread_list):
                thread.terminate()
            self.thread_list.clear()
            logging.info('Killed threads.')
        logging.info('MDGProgressWindow finished.')
        super().destroy()

    def stop_button(self):
        self.main_window.setEnabled(True)
        self.main_window.show()
        self.destroy()

    def closeEvent(self, event):
        if not self.completed:
            reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to quit?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.stop_button()
                event.accept()
            else:
                event.ignore()
        self.stop_button()

    def start_thread(self, thread_class, progress_bar, on_finished, critical_signal=None):
        if not self.isEnabled():
            return
        self.current_progress_bar = progress_bar
        thread = thread_class(copy.deepcopy(self.main_window.serialized_widgets))
        self.thread_list.append(thread)
        thread.progress.connect(self.set_progress)
        thread.progress_bar.connect(self.update_progress_bar)
        thread.finished.connect(on_finished)
        if critical_signal is None:
            thread.critical_signal.connect(self.critical_signal)
        else:
            thread.critical_signal.connect(critical_signal)
        thread.start()
        return thread

    def start(self):
        self.start_thread(InitialisationThread, self.ui.init_progress_bar, self.copy_mods, self.decomp_cmd_check_failed)

    @only_if_window_active
    def copy_mods(self):
        self.start_thread(CopyThread, self.ui.copy_progress_bar, self.init_mdk)

    @only_if_window_active
    def init_mdk(self):
        self.start_thread(MdkInitialisationThread, self.ui.mdk_init_progress_bar, self.deobf_mods)

    @only_if_window_active
    def deobf_mods(self):
        self.start_thread(DeobfuscationMainThread, self.ui.deobf_progress_bar, self.decomp_mods)

    @only_if_window_active
    def decomp_mods(self):
        self.start_thread(DecompilationMainThread, self.ui.decomp_progress_bar, self.merge_mods)

    @only_if_window_active
    def merge_mods(self):
        self.start_thread(MergingThread, self.ui.merge_progress_bar, self.complete)

    @only_if_window_active
    def complete(self):
        self.ui.stop_button.setText('exit')
        self.completed = True
        pass

    def set_progress(self, value, text):
        self.current_progress_bar.setValue(value)
        self.ui.currently_label.setText(text)

    def append_logger(self, color, msg):
        is_down = False
        scrollbar = self.ui.logger_text_edit.verticalScrollBar()
        if scrollbar.value() == scrollbar.maximum():
            is_down = True

        cursor = self.ui.logger_text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.movePosition(QTextCursor.End)

        line_format = cursor.charFormat()
        line_format.setForeground(QColor(color))
        cursor.setCharFormat(line_format)

        cursor.insertText(msg)
        cursor.insertText('\n')

        if is_down:
            scrollbar.setValue(scrollbar.maximum())

    def update_progress_bar(self, i):
        self.current_progress_bar.setValue(i)

    def critical_signal(self, s1, s2):
        self.main_window.mb = CriticalMBThread(s1, s2)
        self.main_window.mb.critical_signal.connect(self.main_window.critical_from_progress_window)
        self.main_window.mb.start()
        self.destroy()

    def decomp_cmd_check_failed(self, s1, s2):
        self.main_window.mb = CriticalMBThread(s1, s2)
        self.main_window.mb.critical_signal.connect(self.main_window.decomp_cmd_check_failed)
        self.main_window.mb.start()
        self.destroy()
