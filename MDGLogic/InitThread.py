import os

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil import FileUtils


class InitThread(AbstractMDGThread):
    decomp_cmd_check_failed = Signal()


    def __init__(self, decomp_cmd: str):
        super().__init__()
        self.decomp_cmd = decomp_cmd

    def run(self):
        self.progress.emit(10, "Clearing tmp folders")
        FileUtils.clear_tmp_folders()

        self.progress.emit(10, "Checking decompiler/decompiler cmd is correct")
        try:
            os.system(self.decomp_cmd.format(path_to_jar='decompiler/decompiler_test_mod.jar', out_path='tmp/decompiler_test'))
            assert len(os.listdir('tmp/decompiler_test')) >= 1
        except Exception:
            self.decomp_cmd_check_failed.emit()
            return

        self.progress.emit(40, "Clearing result folders")
        FileUtils.clear_result_folders()

        self.progress.emit(70, "Creating new folders")
        FileUtils.init_folders()

        self.progress.emit(100, "Initialisation complete")
