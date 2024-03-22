import os
import shutil

from MDGUtil import PathUtils, FileUtils

VERSION = '2.2.4'


def main():
    os.system('flake8')
    FileUtils.remove_folder('build')
    FileUtils.remove_folder('dist')
    FileUtils.remove_folder(PathUtils.RESULT_FOLDER_PATH)
    FileUtils.remove_folder(PathUtils.TMP_FOLDER_PATH)
    FileUtils.remove_folder(os.path.join(PathUtils.DECOMPILER_FOLDER_PATH, 'data'))
    file_name = f'MDG_{VERSION}'
    file_name_with_extension = file_name + '.exe'
    os.system(f'.venv\\Scripts\\activate && pyinstaller.exe MDG.py --onefile --name {file_name}')
    shutil.copytree(PathUtils.DECOMPILER_FOLDER_PATH, os.path.join('dist', 'MDG', 'decompiler'))
    shutil.move(os.path.join('dist', file_name_with_extension), os.path.join('dist', 'MDG', file_name_with_extension))
    shutil.make_archive(f'mods_decompiler_GUI_{VERSION}', 'zip', os.path.join('dist'))
    FileUtils.remove_folder('dist')
    FileUtils.remove_folder('build')


if __name__ == '__main__':
    main()
