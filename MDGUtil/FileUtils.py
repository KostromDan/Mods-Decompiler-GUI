import os
import shutil

from MDGUtil import PathUtils


def remove_folder(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def create_folder(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def clear_tmp_folders():
    remove_folder(PathUtils.TMP_FOLDER_PATH)


def create_tmp_folders():
    create_folder(PathUtils.TMP_FOLDER_PATH)


def create_result_folders():
    create_folder(PathUtils.RESULT_FOLDER_PATH)


def clear_result_folders():
    remove_folder(PathUtils.RESULT_FOLDER_PATH)


def init_folders():
    create_result_folders()
    create_tmp_folders()


def clear_folders():
    clear_tmp_folders()
    clear_result_folders()
