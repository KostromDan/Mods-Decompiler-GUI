import logging
import os

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil import FileUtils


class InitThread(AbstractMDGThread):
    decomp_cmd_check_failed = Signal()

    def run(self):
        decomp_cmd = self.serialized_widgets['decomp_cmd_line_edit']['text']
        if self.serialized_widgets['decomp_cmd_groupbox']['isEnabled']:
            self.progress.emit(10, "Checking decompiler/decompiler cmd are correct")
            try:
                os.system(decomp_cmd.format(path_to_jar='decompiler/decompiler_test_mod.jar',
                                            out_path='tmp/decompiler_test'))
                assert len(os.listdir('tmp/decompiler_test')) >= 1
            except Exception:
                self.decomp_cmd_check_failed.emit()
                return
            logging.info("Checked decompiler/decompiler cmd are correct successfully.")

        self.progress.emit(40, "Clearing tmp folder")
        FileUtils.clear_tmp_folders()
        logging.info("Cleared tmp folders.")

        self.progress.emit(50, "Clearing result folder")
        FileUtils.clear_result_folders()
        logging.info("Cleared result folders.")

        self.progress.emit(80, "Creating new folders")
        FileUtils.init_folders()
        logging.info("Created new folders.")

        self.progress.emit(100, "Initialisation complete")
        logging.info("Initialisation completed.")
