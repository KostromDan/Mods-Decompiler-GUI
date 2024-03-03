import faulthandler
import sys

from PySide6.QtWidgets import QApplication

from MDGUtil.MDGLogger import MDGLogger
from MDGWindow.MDGMainWindow import MDGMainWindow

if __name__ == '__main__':
    MDGLogger()
    faulthandler.enable()
    app = QApplication(sys.argv)
    widget = MDGMainWindow()
    widget.show()
    sys.exit(app.exec())
