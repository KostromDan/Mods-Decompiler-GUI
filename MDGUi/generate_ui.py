import os
import subprocess

from MDGUtil import FileUtils


def run_from_current_path(cmd: str) -> None:
    subprocess.Popen(cmd, cwd=os.path.dirname(__file__)).wait()


def generate_ui() -> None:
    FileUtils.create_folder(os.path.join(os.path.dirname(__file__), 'generated'))
    run_from_current_path('pyside6-uic forms/MDGMainWindow.ui -o generated/Ui_MDGMainWindow.py --from-imports')
    run_from_current_path('pyside6-uic forms/MDGHelpWindow.ui -o generated/Ui_MDGHelpWindow.py --from-imports')
    run_from_current_path('pyside6-uic forms/MDGProgressWindow.ui -o generated/Ui_MDGProgressWindow.py --from-imports')
    run_from_current_path('pyside6-uic forms/MDGMdkWindow.ui -o generated/Ui_MDGMdkWindow.py --from-imports')
    run_from_current_path('pyside6-uic forms/MDGResultWindow.ui -o generated/Ui_MDGResultWindow.py --from-imports')
    run_from_current_path('pyside6-rcc resources.qrc -o generated/resources_rc.py')


if __name__ == '__main__':
    generate_ui()
