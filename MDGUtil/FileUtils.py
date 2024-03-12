import os
import shutil

from MDGUtil import PathUtils


def remove_folder(path: str | os.PathLike) -> None:
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def create_folder(path: str | os.PathLike) -> None:
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def clear_tmp_folders() -> None:
    remove_folder(PathUtils.TMP_FOLDER_PATH)


def create_tmp_folders() -> None:
    create_folder(PathUtils.TMP_FOLDER_PATH)


def create_result_folders() -> None:
    create_folder(PathUtils.RESULT_FOLDER_PATH)


def clear_result_folders() -> None:
    remove_folder(PathUtils.RESULT_FOLDER_PATH)


def init_folders() -> None:
    create_result_folders()
    create_tmp_folders()


def clear_folders() -> None:
    clear_tmp_folders()
    clear_result_folders()
