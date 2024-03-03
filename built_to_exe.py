import os
import shutil

from MDGUtil.FileUtils import remove_folder

VERSION = '2.0.1'


def main():
    remove_folder('build')
    remove_folder('dist')
    remove_folder('result')
    remove_folder('tmp')
    os.system('venv\\Scripts\\activate && pyinstaller.exe MDG.py')
    shutil.copytree('images', os.path.join('dist', 'MDG', 'images'))
    shutil.copytree('decompiler', os.path.join('dist', 'MDG', 'decompiler'))
    shutil.make_archive(f'mods_decompiler_GUI_{VERSION}', 'zip', os.path.join('dist'))


if __name__ == '__main__':
    main()
