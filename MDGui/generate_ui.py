import os
import sys

if not (getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')):  # not inside PyInstaller
    os.system("pyside6-uic MDGMainWindow.ui -o Ui_MDGMainWindow.py")
    os.system("pyside6-uic MDGHelpWindow.ui -o Ui_MDGHelpWindow.py")