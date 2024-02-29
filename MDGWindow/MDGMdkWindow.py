# This Python file uses the following encoding: utf-8
import webbrowser

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

from MDGui.Ui_MDGMdkWindow import Ui_MDGMdkWindow


class MDGMdkWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MDGMdkWindow()
        self.ui.setupUi(self)

        self.ui.forge_button.clicked.connect(self.open_minecraft_forge)
        self.ui.close_button.clicked.connect(self.hide)

        self.ui.label.setPixmap(QPixmap(u"images/mdk_instruction.png"))

        self.setFixedSize(self.minimumSizeHint().width(), self.minimumSizeHint().height())

    def open_minecraft_forge(self):
        webbrowser.open('https://files.minecraftforge.net/net/minecraftforge/forge/')
