import os
import shutil

from main import del_folder


def main():
    del_folder("build")
    del_folder("dist")
    del_folder("mdk")
    del_folder("result")
    os.system("venv\\Scripts\\activate && pyinstaller.exe main.py")
    os.system("xcopy.exe .\\mdk_instruction.png .\\dist\\main\\")
    shutil.make_archive("mods_decompiler_GUI", 'zip', os.path.join('dist'))


if __name__ == "__main__":
    main()
