import logging
import os
import shutil

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil.FileUtils import create_folder

SKIP = [
    '.cache',
    'win32-x86-64',
    'win32-x86',
    'linux-x86-64',

]
TO_RESOURCES = [
    'assets',
    'data',
    'META-INF',
    'spectrelib',
    'reports',
    'modernfix',
    'licenses',
    'kubejsadditions',
    'google',
    'coremods',
]


class MergingThread(AbstractMDGThread):
    def run(self):
        if not self.serialized_widgets['merge_check_box']['isChecked'] or not \
                self.serialized_widgets['merge_check_box']['isEnabled']:
            self.progress.emit(100, 'Merging skipped.')
            logging.info('Merging skipped.')
            return

        logging.info('Merging started.')
        self.progress.emit(0, 'Merging started.')

        mods_path = os.path.join('result', 'decompiled_mods')
        mods_count = len(mods_path)

        merge_code = self.serialized_widgets['merge_code_check_box']['isChecked']
        merge_resources = self.serialized_widgets['merge_resources_check_box']['isChecked']

        shutil.rmtree('result/merged_mdk/src/main')
        create_folder('result/merged_mdk/src/main')

        for n, decompiled_mod in enumerate(os.listdir(mods_path)):
            path_to_mod = os.path.join(mods_path, decompiled_mod)
            if os.path.isfile(path_to_mod):
                continue
            self.progress.emit(int((n / mods_count) * 100), f'Started merging of {decompiled_mod}.')
            logging.info(f'Started merging of {decompiled_mod}.')
            for file in os.listdir(path_to_mod):
                path_to_file = os.path.join(path_to_mod, file)
                if file in SKIP:
                    continue
                if os.path.isfile(path_to_file) or file in TO_RESOURCES:
                    if merge_resources:
                        if os.path.isdir(path_to_file):
                            shutil.copytree(path_to_file, f'result/merged_mdk/src/main/resources/{file}',
                                            dirs_exist_ok=True)
                        else:
                            create_folder('result/merged_mdk/src/main/resources')
                            shutil.copy(path_to_file, 'result/merged_mdk/src/main/resources')
                    continue
                if file == 'resources':
                    if merge_resources:
                        shutil.copytree(path_to_file, 'result/merged_mdk/src/main/resources', dirs_exist_ok=True)
                    continue
                if merge_code and '_common_' not in file:
                    shutil.copytree(path_to_file, f'result/merged_mdk/src/main/java/{file}', dirs_exist_ok=True)

        logging.info('Merging complete.')
        self.progress.emit(100, 'Merging complete.')
