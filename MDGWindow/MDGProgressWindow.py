# This Python file uses the following encoding: utf-8
import copy
import logging
import sys
from typing import Callable, Optional

from MDGUi.generated.Ui_MDGProgressWindow import Ui_MDGProgressWindow
from PySide6.QtCore import QThread
from PySide6.QtGui import QTextCursor, QColor, QCloseEvent
from PySide6.QtWidgets import QMainWindow, QMessageBox, QProgressBar

from MDGLogic.CopyThread import CopyThread
from MDGLogic.CriticalMBThread import CriticalMBThread
from MDGLogic.DecompilationMainThread import DecompilationMainThread
from MDGLogic.DeobfuscationThread import DeobfuscationThread, FailLogic
from MDGLogic.InitialisationThread import InitialisationThread
from MDGLogic.MdkInitialisationThread import MdkInitialisationThread
from MDGLogic.MergingThread import MergingThread
from MDGUtil import FileUtils
from MDGUtil.MDGLogger import MDGLogger
from MDGWindow.MDGResultWindow import MDGResultWindow


def only_if_window_active(func):
    def wrapper(self, *args, **kwargs):
        if self.isEnabled():
            return func(self, *args, **kwargs)

    return wrapper


class MDGProgressWindow(QMainWindow):
    def __init__(self, main_window) -> None:
        super().__init__()
        self.ui = Ui_MDGProgressWindow()
        self.ui.setupUi(self)

        self.main_window = main_window

        self.thread_list = []
        self.current_progress_bar = self.ui.init_progress_bar

        self.ui.stop_button.clicked.connect(self.stop_button)

        MDGLogger().logger_signal.append_logger_signal.connect(self.append_logger)

        self.completed = False

        self.failed_deobfuscation_mods = []
        self.failed_decompilation_mods = []
        self.fail_logic = None

        self.result_window = None

        logging.info('Progress window started.')

    def destroy(self, *args, **kwargs) -> None:
        self.setEnabled(False)
        if len(self.thread_list) >= 1:
            logging.info('Killing threads.')
            for thread in reversed(self.thread_list):
                thread.terminate()
            self.thread_list.clear()
            logging.info('Killed threads.')
        logging.info('MDGProgressWindow finished.')
        super().destroy(*args, **kwargs)

    def stop_button(self) -> None:
        self.main_window.setEnabled(True)
        self.main_window.show()
        if self.completed:
            sys.exit()
        self.destroy()

    def closeEvent(self, event: QCloseEvent) -> None:
        if not self.completed:
            reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to quit?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.stop_button()
                event.accept()
            else:
                event.ignore()
                return
        self.stop_button()
        event.accept()

    def start_thread(self,
                     thread_class: QThread.__class__,
                     progress_bar: QProgressBar,
                     on_finished: Callable,
                     thread_signals: dict[str: Callable] = None) -> Optional[QThread]:
        if not self.isEnabled():
            return
        if thread_signals is None:
            thread_signals = dict()
        self.current_progress_bar = progress_bar
        thread = thread_class(copy.deepcopy(self.main_window.serialized_widgets))
        self.thread_list.append(thread)
        thread.progress.connect(self.set_progress)
        thread.progress_bar.connect(self.update_progress_bar)
        thread.finished.connect(on_finished)
        thread.critical_signal.connect(self.critical_signal)

        for signal, func in thread_signals.items():
            getattr(thread, signal).connect(func)
        thread.start()
        return thread

    def start(self) -> None:
        self.start_thread(InitialisationThread, self.ui.init_progress_bar, self.copy_mods)

    @only_if_window_active
    def copy_mods(self) -> None:
        self.start_thread(CopyThread, self.ui.copy_progress_bar, self.init_mdk, thread_signals={
            'use_cached_signal': self.set_use_cached
        })

    @only_if_window_active
    def init_mdk(self) -> None:
        self.start_thread(MdkInitialisationThread, self.ui.mdk_init_progress_bar, self.deobf_mods)

    @only_if_window_active
    def deobf_mods(self) -> None:
        self.start_thread(DeobfuscationThread, self.ui.deobf_progress_bar, self.decomp_mods, thread_signals={
            'failed_mod_signal': self.failed_deobf_mod,
            'fail_logic_signal': self.set_fail_logic
        })

    @only_if_window_active
    def decomp_mods(self) -> None:
        self.start_thread(DecompilationMainThread, self.ui.decomp_progress_bar, self.merge_mods, thread_signals={
            'failed_mod_signal': self.failed_decomp_mod,
        })

    @only_if_window_active
    def merge_mods(self) -> None:
        self.start_thread(MergingThread, self.ui.merge_progress_bar, self.complete)

    @only_if_window_active
    def complete(self) -> None:
        FileUtils.remove_folder('tmp')
        self.ui.stop_button.setText('exit')
        self.completed = True
        self.setEnabled(False)
        self.hide()
        self.result_window = MDGResultWindow(self)
        self.result_window.show()

    def set_progress(self, value: int, text: str) -> None:
        self.current_progress_bar.setValue(value)
        self.ui.currently_label.setText(text)

    def append_logger(self, color: str, msg: str) -> None:
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

    def update_progress_bar(self, value: int) -> None:
        self.current_progress_bar.setValue(value)

    def critical_signal(self, title: str, text: str, main_window_widget_name: str = None) -> None:
        self.main_window.mb = CriticalMBThread(title, text, main_window_widget_name)
        self.main_window.mb.critical_signal.connect(self.main_window.critical_from_progress_window)
        self.main_window.mb.start()
        self.destroy()

    def failed_deobf_mod(self, mod: str) -> None:
        self.failed_deobfuscation_mods.append(mod)

    def failed_decomp_mod(self, mod: str) -> None:
        self.failed_decompilation_mods.append(mod)

    def set_fail_logic(self, logic: FailLogic) -> None:
        self.fail_logic = logic

    def set_use_cached(self, use_cached: list[str]) -> None:
        self.main_window.serialized_widgets['use_cached'] = use_cached
