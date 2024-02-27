# This Python file uses the following encoding: utf-8
import os
import sys
import webbrowser

from PySide6.QtWidgets import QApplication, QMainWindow

from MDGUtils.LocalConfig import LocalConfig
from MDGUi.Ui_MDGHelpWindow import Ui_MDGHelpWindow


class MDGHelpWindow(QMainWindow):
    was_decomp_enabled = False
    config = LocalConfig()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MDGHelpWindow()
        self.ui.setupUi(self)

        self.ui.mdk_button.clicked.connect(self.open_minecraft_forge)

    def open_minecraft_forge(self):
        webbrowser.open('https://files.minecraftforge.net/net/minecraftforge/forge/')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MDGHelpWindow()
    widget.show()
    sys.exit(app.exec())
