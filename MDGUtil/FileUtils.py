import filecmp
import logging
import os
import shutil
import zipfile
from typing import Iterator

from MDGUtil import PathUtils


def walk_in_zipfile(zip_ref: zipfile.ZipFile) -> Iterator[str]:
    info_list = zip_ref.infolist()
    for file_info in info_list:
        if not file_info.filename.endswith('/'):
            yield file_info.filename


def extract_jars_from_jar(jar_path: str | os.PathLike,
                          extract_to: str | os.PathLike) -> None:
    with zipfile.ZipFile(jar_path, 'r') as zip_ref:
        for file in walk_in_zipfile(zip_ref):
            if file.endswith('.jar'):
                zip_ref.extract(file, extract_to)

                iter_count = 0
                old_jar_path = os.path.join(extract_to, file)
                while True:
                    suffix = (f'_{iter_count}' if iter_count > 0 else '') + '.jar'
                    new_file_name = os.path.basename(file).replace(' ','_').removesuffix('.jar')
                    new_jar_path = os.path.join(extract_to, new_file_name) + suffix
                    try:
                        os.rename(old_jar_path, new_jar_path)
                        break
                    except FileExistsError:
                        if filecmp.cmp(old_jar_path, new_jar_path):
                            break
                        iter_count += 1
                logging.info(f'Found and extracted {new_file_name} from {os.path.basename(jar_path)}')
                path_elements = file.split('/')
                if len(path_elements) != 1:
                    shutil.rmtree(os.path.join(extract_to, path_elements[0]))
                extract_jars_from_jar(new_jar_path, extract_to)  # Extract jar in jar in jar and so on


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
