import logging
import os
import time

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil import FileUtils


class InitThread(AbstractMDGThread):
    decomp_cmd_check_failed = Signal()

    def __init__(self, decomp_cmd: str):
        super().__init__()
        self.decomp_cmd = decomp_cmd

    def run(self):
        self.progress.emit(10, "Checking decompiler/decompiler cmd is correct")
        try:
            os.system(self.decomp_cmd.format(path_to_jar='decompiler/decompiler_test_mod.jar',
                                             out_path='tmp/decompiler_test'))
            assert len(os.listdir('tmp/decompiler_test')) >= 1
        except Exception:
            self.decomp_cmd_check_failed.emit()
            return
        logging.info("Checking decompiler/decompiler cmd is correct: Success.")

        self.progress.emit(10, "Clearing tmp folders")
        FileUtils.clear_tmp_folders()
        logging.info("Cleared tmp folders.")

        self.progress.emit(50, "Clearing result folders")
        FileUtils.clear_result_folders()
        logging.info("Cleared result folders.")

        time.sleep(5)

        self.progress.emit(80, "Creating new folders")
        FileUtils.init_folders()
        logging.info("Created new folders.")

        self.progress.emit(100, "Initialisation complete")
        logging.info("Initialisation completed.")
