import os
import shutil

from MDGUtil.FileUtils import remove_folder

VERSION = '2.1.0'


def main():
    remove_folder('build')
    remove_folder('dist')
    remove_folder('result')
    remove_folder('tmp')
    file_name = f'MDG_{VERSION}'
    file_name_with_extension = file_name+'.exe'
    os.system(f'venv\\Scripts\\activate && pyinstaller.exe MDG.py --onefile --name {file_name}')
    shutil.copytree('images', os.path.join('dist', 'MDG', 'images'))
    shutil.copytree('decompiler', os.path.join('dist', 'MDG', 'decompiler'))
    shutil.move(os.path.join('dist', file_name_with_extension), os.path.join('dist', 'MDG',file_name_with_extension))
    shutil.make_archive(f'mods_decompiler_GUI_{VERSION}', 'zip', os.path.join('dist'))


if __name__ == '__main__':
    main()
