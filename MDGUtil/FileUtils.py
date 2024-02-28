import os
import shutil


def remove_folder(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def clear_tmp_folders():
    remove_folder('tmp')


def clear_result_folders():
    remove_folder('result')


def init_folders():
    os.mkdir('tmp')
    os.mkdir('result')


def clear_folders():
    clear_tmp_folders()
    clear_result_folders()
