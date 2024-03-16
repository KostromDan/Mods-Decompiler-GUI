import os


def from_imports_replacement(resource_file: str) -> None:
    """Since --from-imports arg for pyside6-rcc in pyside6 is removed,
    but we still need it because of module structure of this project,
    this function replaces it."""
    for file in os.listdir():
        if file.startswith('Ui_') and file.endswith('.py'):
            with open(file, 'r') as f:
                file_content = f.read()
            file_content = file_content.replace(f'import {resource_file}',
                                                f'from . import {resource_file}')
            with open(file, 'w') as f:
                f.write(file_content)


if __name__ == '__main__':
    os.system('pyside6-uic MDGMainWindow.ui -o Ui_MDGMainWindow.py')
    os.system('pyside6-uic MDGHelpWindow.ui -o Ui_MDGHelpWindow.py')
    os.system('pyside6-uic MDGProgressWindow.ui -o Ui_MDGProgressWindow.py')
    os.system('pyside6-uic MDGMdkWindow.ui -o Ui_MDGMdkWindow.py')
    os.system('pyside6-uic MDGResultWindow.ui -o Ui_MDGResultWindow.py')
    os.system('pyside6-rcc -o resources_rc.py resources.qrc')
    from_imports_replacement('resources_rc')
