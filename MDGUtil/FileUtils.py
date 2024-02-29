import os
import shutil


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
    remove_folder('tmp')


def create_tmp_folders():
    create_folder('tmp')


def create_result_folders():
    create_folder('result')


def clear_result_folders():
    remove_folder('result')


def init_folders():
    create_result_folders()
    create_tmp_folders()


def clear_folders():
    clear_tmp_folders()
    clear_result_folders()
