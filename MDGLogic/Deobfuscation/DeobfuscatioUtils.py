import logging
import os
import shutil
from enum import Enum

from MDGUtil import PathUtils


class Status(Enum):
    INTERRUPTED = -2
    FAILED = -1
    CREATED = 0
    STARTED = 1
    SUCCESS = 2


class FailLogic(Enum):
    INTERRUPT = 1
    SKIP = 2
    DECOMPILE = 3


class DeobfuscationAlgorithm(Enum):
    MDK_SAFE = 1
    MDK_FAST = 2
    BON2 = 3


def clear_forge_gradle():
    try:
        for folder in os.listdir(PathUtils.FORGE_GRADLE_DEOBF_CACHE_FOLDER):
            if folder.startswith('local_MDG_'):
                shutil.rmtree(os.path.join(PathUtils.FORGE_GRADLE_DEOBF_CACHE_FOLDER, folder))
    except FileNotFoundError:
        logging.warning(f'Could not find {PathUtils.FORGE_GRADLE_DEOBF_CACHE_FOLDER}. Skipping clearing gradle cache.')
