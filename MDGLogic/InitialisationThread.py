import logging
import os
import subprocess

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil import FileUtils
from MDGUtil.FileUtils import create_folder
from MDGUtil.SubprocessKiller import kill_subprocess


class InitialisationThread(AbstractMDGThread):
    decomp_cmd_check_failed = Signal()

    def run(self):
        decomp_cmd = self.serialized_widgets['decomp_cmd_line_edit']['text']

        self.progress.emit(20, "Clearing tmp folder")
        FileUtils.clear_tmp_folders()
        logging.info("Cleared tmp folders.")

        self.progress.emit(40, "Clearing result folder")
        FileUtils.clear_result_folders()
        logging.info("Cleared result folders.")

        self.progress.emit(50, "Creating new folders")
        FileUtils.init_folders()
        logging.info("Created new folders.")

        if self.serialized_widgets['decomp_cmd_groupbox']['isEnabled']:
            self.progress.emit(80, "Checking decompiler/decompiler cmd are correct")
            create_folder('tmp/decompiler_test')
            decomp_cmd_formatted = decomp_cmd.format(path_to_jar='decompiler/decompiler_test_mod.jar',
                                                     out_path='tmp/decompiler_test')
            print(decomp_cmd_formatted)
            try:
                self.cmd = subprocess.Popen(decomp_cmd_formatted.split(' '), shell=True)
                self.cmd.wait()
                assert len(os.listdir('tmp/decompiler_test')) >= 1
            except Exception:
                self.decomp_cmd_check_failed.emit()
                return
            logging.info("Checked decompiler/decompiler cmd are correct successfully.")

        self.progress.emit(100, "Initialisation complete")
        logging.info("Initialisation completed.")

    def terminate(self):
        kill_subprocess(self.cmd.pid)
        super().terminate()
