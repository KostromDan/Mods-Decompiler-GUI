import os
import re
import shutil
import sys
import threading
import time
import webbrowser
import zipfile
from tkinter import filedialog

from pretty_downloader import pretty_downloader

from gui import *

DECOMPILATION_THREADS = 10
STAGES = 7

mdk_patch_str = """repositories {
    flatDir {
        dir 'libs'
    }
}
dependencies {
    fileTree(include: ['*.jar'], dir: 'libs').each { file ->
        def fileNameWithoutDotJarExtension = file.name.substring(0, file.name.length() - 4)
        def indexOfLastDash = fileNameWithoutDotJarExtension.lastIndexOf('-');
        project.logger.warn("starting deobfuscating ${file.name}")
        implementation fg.deobf("local_mod_source_downloader:${fileNameWithoutDotJarExtension.substring(0, indexOfLastDash)}:${fileNameWithoutDotJarExtension.substring(indexOfLastDash + 1)}")
    }
}"""


def choose_dir(title):
    root = tkinter.Tk()
    root.withdraw()

    path = filedialog.askdirectory(title=title)

    return path


def choose_file(title):
    root = tkinter.Tk()
    root.withdraw()

    path = filedialog.askopenfile(title=title)

    return path.name


def mdk_instruction():
    window = tkinter.Tk()
    window.title("MDK instruction")

    def on_ok_click():
        window.destroy()

    def open_minecraftforge():
        webbrowser.open('https://files.minecraftforge.net/')

    image = tkinter.PhotoImage(file="mdk_instruction.png")

    label = tkinter.Label(window, image=image)
    label.pack()

    label_text = tkinter.Label(window, text="This programm needs archive with forge MDK for correct work. "
                                            "Download it from the MinecraftForge website. "
                                            "In the next step, the program will ask you to select it.\n"
                                            "Make sure what version of Forge, you using to launch your game and Forge MDK are same.")
    label_text.pack()

    minecraftforge_button = tkinter.Button(window, text="Open MinecraftForge website", command=open_minecraftforge)
    minecraftforge_button.pack()

    ok_button = tkinter.Button(window, text="ОК", command=on_ok_click)
    ok_button.pack()

    window.mainloop()


def patch_mdk():
    with open('mdk/build.gradle', 'r') as file:
        if mdk_patch_str in file.read():
            return
    with open('mdk/build.gradle', 'a') as file:
        file.write(mdk_patch_str)


def copy_mods(mods_dir_path, window):
    libs_path = os.path.join('mdk', 'libs')
    os.makedirs(libs_path, exist_ok=True)
    count = len(os.listdir(mods_dir_path))
    for i, mod in enumerate(os.listdir(mods_dir_path)):
        new_name, n = re.subn(' |_', '-', mod)
        window.update_task_text(f"Copying {new_name}")
        shutil.copyfile(os.path.join(mods_dir_path, mod), os.path.join(libs_path, new_name))
        window.update_task_value(int((i / count) * 100))


def decompile_mod(path_to_jar, out_path):
    os.system(fr'java -jar vineflower-1.9.3.jar -dgs=1 {path_to_jar} .\{out_path}')
    print(f"decompilation finished: {path_to_jar}")


def get_active_count(threads):
    count = 0
    for thread in threads:
        if thread.is_alive():
            count += 1
    return count


def decompile_update_window(window, threads, mods_count, count):
    cur_count = 0
    for thread in threads:
        if not thread.is_alive():
            cur_count += 1
    if count != cur_count:
        count = cur_count
        window.update_task_value(int((count / mods_count) * 100))
        window.update_task_text(f"Decompiled {count}/{mods_count}")
    return count


def decompile_mods(deobfed_mods_path, mods_path, window):
    os.makedirs("result", exist_ok=True)
    threads = []
    count = 0
    mods_count = len(os.listdir(mods_path))
    for mod_dir in os.listdir(deobfed_mods_path):
        dir_2 = os.path.join(deobfed_mods_path, mod_dir)
        jar_dir = os.path.join(dir_2, os.listdir(dir_2)[0])
        for file in os.listdir(jar_dir):
            if file.endswith('.jar'):
                path_to_jar = os.path.join(jar_dir, file)
                print(f"decompilation started: {path_to_jar}")
                out_dir_name = file.split('_mapped_official')[0]
                while get_active_count(threads) >= DECOMPILATION_THREADS:
                    time.sleep(0.1)
                thread = threading.Thread(target=decompile_mod, args=(path_to_jar, os.path.join('result', out_dir_name)))
                threads.append(thread)
                thread.start()
                break
        count = decompile_update_window(window, threads, mods_count, count)

    while get_active_count(threads) != 0:
        count = decompile_update_window(window, threads, mods_count, count)


def download_vineflower():
    pretty_downloader.download('https://github.com/Vineflower/vineflower/releases/download/1.9.3/vineflower-1.9.3.jar')


def merge_all_mods_into_mdk(window):
    skip = [
        ".cache",
        "win32-x86-64",
        "win32-x86",
        "linux-x86-64",

    ]
    to_resources = [
        "assets",
        "data",
        "META-INF",
        "spectrelib",
        "reports",
        "modernfix",
        "licenses",
        "kubejsadditions",
        "google",
        "coremods",
    ]
    mods_count = len(os.listdir('result'))

    copy_assets = window.copy_assets

    window.update_progress_text("Merging mods")
    window.update_progress_value(int((7 * 100) / STAGES))
    window.update_task_text("")
    window.update_task_value(0)

    for k, mod in enumerate(os.listdir('result')):
        print(mod)
        window.update_task_value(int(((k + 1) / mods_count) * 100))
        window.update_task_text(f"Merged {k + 1}/{mods_count}")

        for i in os.listdir(os.path.join('result', mod)):
            if i in skip:
                continue
            path = os.path.join('result', mod, i)
            if os.path.isfile(path) or i in to_resources:
                if copy_assets:
                    if os.path.isfile(path):
                        pass
                        os.system(fr'echo F|xcopy.exe .\{path} .\mdk\src\main\resources\{i} /F /S /Y /E')
                    else:
                        pass
                        os.system(fr'echo D|xcopy.exe .\{path}\* .\mdk\src\main\resources\{i} /F /S /Y /E')
                continue
            if i == "resources":
                if copy_assets:
                    os.system(fr'echo D|xcopy.exe .\{path}\* .\mdk\src\main\{i} /F /S /Y /E')
                continue
            if not '_common_' in i:
                os.system(fr'echo D|xcopy.exe .\{path}\* .\mdk\src\main\java\{i} /F /S /Y /E')


def deobf():
    os.system('cd mdk &&  .\gradlew.bat build')
    shutil.rmtree(os.path.join('mdk', 'libs'))


def deobf_mods(window, deobfed_mods_path, mods_path):
    try:
        shutil.rmtree(deobfed_mods_path)
    except FileNotFoundError:
        pass
    thread = threading.Thread(target=deobf)
    thread.start()

    count = 0
    mods_count = len(os.listdir(mods_path))
    value = 0
    while count != mods_count and thread.is_alive():
        try:
            count = len(os.listdir(deobfed_mods_path))
            old_value = value
            value = int((count / mods_count) * 100)
            if value != old_value:
                window.update_task_value(value)
                window.update_task_text(f"Deobfuscated {count}/{mods_count}")
        except FileNotFoundError:
            time.sleep(0.5)
    thread.join()


def start(mods_path, mdk_path, deobfed_mods_path, window):
    window.update_progress_text("Unzipping mdk")
    window.update_progress_value(int((1 * 100) / STAGES))

    with zipfile.ZipFile(mdk_path, 'r') as zip_ref:
        zip_ref.extractall("mdk")

    window.update_progress_text("Patching mdk")
    window.update_progress_value(int((2 * 100) / STAGES))

    patch_mdk()

    window.update_progress_text("Copying mods")
    window.update_progress_value(int((3 * 100) / STAGES))

    copy_mods(mods_path, window)

    window.update_progress_text("Deobfuscating mods")
    window.update_progress_value(int((4 * 100) / STAGES))
    window.update_task_text("")
    window.update_task_value(0)

    deobf_mods(window, deobfed_mods_path, mods_path)

    window.update_progress_text("Downloading vineflower")
    window.update_progress_value(int((5 * 100) / STAGES))
    window.update_task_text("")
    window.update_task_value(50)

    download_vineflower()

    window.update_progress_text("Decompilating mods")
    window.update_progress_value(int((6 * 100) / STAGES))
    window.update_task_text("")
    window.update_task_value(0)

    decompile_mods(deobfed_mods_path, mods_path, window)
    shutil.rmtree(deobfed_mods_path)

    window.merge_mods_ask()
    while window.do_merge is None:
        threading.Event().wait(1)
    if window.do_merge:
        window.include_assets_ask()
        while window.copy_assets is None:
            threading.Event().wait(1)
        merge_all_mods_into_mdk(window)

    window.update_progress_value(100)
    window.update_task_value(100)
    window.create_warn_window("Finished!\n"
                              "See result and mdk folders.")

    print("Finished with success!")
    window.destroy()
    sys.exit()


def del_folder(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def main():
    debug = True
    if not debug:
        mdk_instruction()
        mdk_path = choose_file("Select mdk")
        mods_path = choose_dir("Select mods folder")
    else:
        mdk_instruction()
        mdk_path = "C:/Users/Даниил/Downloads/forge-1.19.2-43.2.23-mdk.zip"
        mods_path = "C:/curseforge/minecraft/Instances/wwoo/mods"

    deobfed_mods_path = os.path.join(os.path.join(os.path.expanduser('~'),
                                                  '.gradle',
                                                  'caches',
                                                  'forge_gradle',
                                                  'deobf_dependencies',
                                                  'local_mod_source_downloader'))

    del_folder("mdk")
    del_folder('result')
    del_folder(deobfed_mods_path)

    if mods_path is None or mdk_path is None:
        raise InterruptedError("Path is None!")

    window = ProgressWindow()

    thread = threading.Thread(target=start, args=(mods_path, mdk_path, deobfed_mods_path, window))
    thread.start()

    window.start()


if __name__ == '__main__':
    main()
