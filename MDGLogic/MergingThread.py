import logging
import os
import shutil

from MDGLogic.AbstractMDGThread import AbstractMDGThread

SKIP = [
    ".cache",
    "win32-x86-64",
    "win32-x86",
    "linux-x86-64",

]
TO_RESOURCES = [
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


# def merge_all_mods_into_mdk(window):
#
#     mods_count = len(os.listdir('result'))
#
#     copy_assets = window.copy_assets
#
#     window.update_progress_text("Merging mods")
#     window.update_progress_value(int((7 * 100) / STAGES))
#     window.update_task_text("")
#     window.update_task_value(0)
#
#     for k, mod in enumerate(os.listdir('result')):
#         print(mod)
#         window.update_task_value(int(((k + 1) / mods_count) * 100))
#         window.update_task_text(f"Merged {k + 1}/{mods_count}")
#
#         for i in os.listdir(os.path.join('result', mod)):
#             if i in SKIP:
#                 continue
#             path = os.path.join('result', mod, i)
#             if os.path.isfile(path) or i in TO_RESOURCES:
#                 if copy_assets:
#                     if os.path.isfile(path):
#                         pass
#                         os.system(fr'echo F|xcopy.exe .\{path} .\mdk\src\main\resources\{i} /F /S /Y /E')
#                     else:
#                         pass
#                         os.system(fr'echo D|xcopy.exe .\{path}\* .\mdk\src\main\resources\{i} /F /S /Y /E')
#                 continue
#             if i == "resources":
#                 if copy_assets:
#                     os.system(fr'echo D|xcopy.exe .\{path}\* .\mdk\src\main\{i} /F /S /Y /E')
#                 continue
#             if not '_common_' in i:
#                 os.system(fr'echo D|xcopy.exe .\{path}\* .\mdk\src\main\java\{i} /F /S /Y /E')
class MergingThread(AbstractMDGThread):
    def run(self):
        if not self.serialized_widgets['merge_check_box']['isChecked'] or not \
                self.serialized_widgets['merge_check_box']['isEnabled']:
            self.progress.emit(100, "Merging skipped.")
            logging.info("Merging skipped.")
            return

        logging.info('Merging started.')
        self.progress.emit(0, "Merging started.")

        mods_path = os.path.join('result', 'decompiled_mods')
        mods_count = len(mods_path)

        merge_code = self.serialized_widgets['merge_code_check_box']['isChecked']
        merge_resources = self.serialized_widgets['merge_resources_check_box']['isChecked']

        for n, decompiled_mod in enumerate(os.listdir(mods_path)):
            self.progress.emit((n / mods_count) * 100, f"Started merging of {decompiled_mod}.")
            path_to_mod = os.path.join(mods_path, decompiled_mod)
            for file in os.listdir(path_to_mod):
                path_to_file = os.path.join(path_to_mod, file)
                if file in SKIP:
                    continue
                if os.path.isfile(path_to_file) or file in TO_RESOURCES:
                    if merge_resources:
                        if os.path.isdir(path_to_file):
                            shutil.copytree(path_to_file, f'result/merged_mdk/src/main/resources/{file}',dirs_exist_ok=True)
                        else:
                            shutil.copy(path_to_file, 'result/merged_mdk/src/main/resources')
                    continue
                if file == 'resources':
                    if merge_resources:
                        shutil.copy(path_to_file, 'result/merged_mdk/src/main/resources')
                    continue
                if merge_code and not '_common_' in file:
                    shutil.copytree(path_to_file, f'result/merged_mdk/src/main/java/{file}',dirs_exist_ok=True)

        logging.info('Merging complete.')
        self.progress.emit(100, "Merging complete.")
