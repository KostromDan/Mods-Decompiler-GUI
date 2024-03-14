import logging
import os
import shutil
from pathlib import Path

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil import PathUtils
from MDGUtil.FileUtils import create_folder

SKIP = [
    '.cache',
    'win32-x86-64',
    'win32-x86',
    'linux-x86-64',
]


def contains_java_file(path: str | os.PathLike) -> bool:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.java'):
                return True
    return False


class MergingThread(AbstractMDGThread):
    def run(self) -> None:
        if not self.serialized_widgets['merge_check_box']['isChecked'] or not \
                self.serialized_widgets['merge_check_box']['isEnabled']:
            self.progress.emit(100, 'Merging skipped.')
            logging.info('Merging skipped.')
            return

        logging.info('Merging started.')
        self.progress.emit(0, 'Merging started.')

        mods_path = PathUtils.DECOMPILED_MODS_PATH
        mods_count = len(os.listdir(mods_path))

        merge_code = self.serialized_widgets['merge_code_check_box']['isChecked']
        merge_resources = self.serialized_widgets['merge_resources_check_box']['isChecked']

        shutil.rmtree(PathUtils.MERGED_MDK_SRC_PATH)
        create_folder(PathUtils.MERGED_MDK_SRC_PATH)
        create_folder(PathUtils.MERGED_MDK_RESOURCES_PATH)

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
                if os.path.isfile(path_to_file):
                    if merge_resources:
                        shutil.copy(path_to_file, PathUtils.MERGED_MDK_RESOURCES_PATH)
                    continue
                if file == 'resources':
                    if merge_resources:
                        shutil.copytree(path_to_file, PathUtils.MERGED_MDK_RESOURCES_PATH, dirs_exist_ok=True)
                    continue
                if contains_java_file(path_to_file):
                    if merge_code:
                        shutil.copytree(path_to_file,
                                        os.path.join(PathUtils.MERGED_MDK_JAVA_PATH, file),
                                        dirs_exist_ok=True)
                    continue
                else:
                    if merge_resources:
                        shutil.copytree(path_to_file,
                                        os.path.join(PathUtils.MERGED_MDK_RESOURCES_PATH, file),
                                        dirs_exist_ok=True)
                    continue

        logging.info('Merging complete.')
        self.progress.emit(100, 'Merging complete.')
