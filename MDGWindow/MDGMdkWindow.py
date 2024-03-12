# This Python file uses the following encoding: utf-8
import webbrowser

from MDGUi.Ui_MDGMdkWindow import Ui_MDGMdkWindow
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

from MDGUtil import PathUtils


class MDGMdkWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MDGMdkWindow()
        self.ui.setupUi(self)

        self.ui.forge_button.clicked.connect(self.open_minecraft_forge)
        self.ui.close_button.clicked.connect(self.hide)

        self.ui.label.setPixmap(QPixmap(u'images/mdk_instruction.png'))

        self.setFixedSize(self.minimumSizeHint().width(), self.minimumSizeHint().height())

    def open_minecraft_forge(self) -> None:
        webbrowser.open(PathUtils.MINECRAFT_FORGE_DOWNLOADS_PAGE)
