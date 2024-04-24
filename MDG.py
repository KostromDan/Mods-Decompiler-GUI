import ctypes
import faulthandler
import multiprocessing
import sys

from PySide6.QtWidgets import QApplication

from MDGUi.generate_ui import generate_ui
from MDGUtil import PathUtils
from MDGUtil.MDGLogger import MDGLogger

if __name__ == '__main__':
    multiprocessing.freeze_support()
    faulthandler.enable()

    if PathUtils.check_pyinstaller_env():
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)  # Hide console
    else:
        generate_ui()

    """generate_ui() can change ui so,we need to import MDGMainWindow only after that line"""
    from MDGWindow.MDGMainWindow import MDGMainWindow

    MDGLogger()
    app = QApplication(sys.argv)
    widget = MDGMainWindow()
    widget.show()
    sys.exit(app.exec())
