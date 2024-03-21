from PySide6.QtWidgets import QAbstractButton


def is_checked_and_enabled(widget: QAbstractButton | dict) -> bool:
    if type(widget) is dict:
        return widget['isChecked'] and widget['isEnabled']
    else:
        return widget.isChecked() and widget.isEnabled()
