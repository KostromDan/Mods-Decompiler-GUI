import webbrowser

from PySide6.QtWidgets import QAbstractButton, QMessageBox

from MDGUtil import PathUtils


def is_checked_and_enabled(widget: QAbstractButton | dict) -> bool:
    if type(widget) is dict:
        return widget['isChecked'] and widget['isEnabled']
    else:
        return widget.isChecked() and widget.isEnabled()

def show_java_not_found_message_box():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Java not found")
    msg_box.setText("Can't find java on this computer.\nMDG requires java for correct work.")
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.addButton("OK", QMessageBox.AcceptRole)
    download_button = msg_box.addButton("Download Java", QMessageBox.ActionRole)
    msg_box.exec()

    if msg_box.clickedButton() == download_button:
        url = PathUtils.ADOPTIUM_DOWNLOADS_PAGE
        webbrowser.open(url)
