import faulthandler
import multiprocessing
import sys

from MDGUi.generate_ui import generate_ui
from PySide6.QtWidgets import QApplication

from MDGUtil import PathUtils
from MDGUtil.MDGLogger import MDGLogger

if __name__ == '__main__':
    multiprocessing.freeze_support()

    if not PathUtils.check_pyinstaller_env():
        faulthandler.enable()
        generate_ui()
    """generate_ui() can change ui so,we need to import MDGMainWindow only after that line"""
    from MDGWindow.MDGMainWindow import MDGMainWindow

    MDGLogger()
    app = QApplication(sys.argv)
    widget = MDGMainWindow()
    widget.show()
    sys.exit(app.exec())
