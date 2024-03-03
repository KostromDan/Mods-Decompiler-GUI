import os

if __name__ == '__main__':
    os.system('pyside6-uic MDGMainWindow.ui -o Ui_MDGMainWindow.py')
    os.system('pyside6-uic MDGHelpWindow.ui -o Ui_MDGHelpWindow.py')
    os.system('pyside6-uic MDGProgressWindow.ui -o Ui_MDGProgressWindow.py')
    os.system('pyside6-uic MDGMdkWindow.ui -o Ui_MDGMdkWindow.py')
