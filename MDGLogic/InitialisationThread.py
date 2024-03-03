import logging
import os
import subprocess
import threading
import time

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil import FileUtils
from MDGUtil.FileUtils import create_folder
from MDGUtil.SubprocessKiller import kill_subprocess
from MDGUtil.SubprocessOutsAnalyseThread import SubprocessOutsAnalyseThread
from PySide6.QtCore import QThread


class ExceptionThread(QThread):
    def __init__(self,e):
        super().__init__()
        self.e =e
    def run(self):
        raise self.e

class InitialisationThread(AbstractMDGThread):
    def run(self):
        decomp_cmd = self.serialized_widgets['decomp_cmd_line_edit']['text']

        self.progress.emit(20, 'Clearing tmp folder')
        FileUtils.clear_tmp_folders()
        logging.info('Cleared tmp folders.')

        self.progress.emit(40, 'Clearing result folder')
        FileUtils.clear_result_folders()
        logging.info('Cleared result folders.')

        self.progress.emit(50, 'Creating new folders')
        FileUtils.init_folders()
        logging.info('Created new folders.')

        if self.serialized_widgets['decomp_cmd_groupbox']['isEnabled']:
            self.progress.emit(80, 'Checking decompiler/decompiler cmd are correct')
            logging.info('Checking decompiler/decompiler cmd are correct')
            create_folder('tmp/decompiler_test')
            try:
                decomp_cmd_formatted = decomp_cmd.format(path_to_jar='decompiler/decompiler_test_mod.jar',
                                                         out_path='tmp/decompiler_test')
                self.cmd = subprocess.Popen(decomp_cmd_formatted.split(' '), shell=True,
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                cmd_analyse_thread = SubprocessOutsAnalyseThread(self.cmd)
                cmd_analyse_thread.start()
                cmd_analyse_thread.join()
                assert len(os.listdir('tmp/decompiler_test')) >= 1
            except Exception as e:
                thread = ExceptionThread(e)
                thread.start()
                time.sleep(0.1)
                self.critical_signal.emit('Incorrect decompiler cmd',
                                          "With this decompiler/decompiler cmd program won't work.\n"
                                          'This message indicates that {path_to_jar} is not decompiled to {out_path}.\n'
                                          'Check decompiler/decompiler cmd: path, syntax, etc. And try again.\n'
                                          'Open the lastest log for more details.\n')
                return
            logging.info('Checked decompiler/decompiler cmd are correct successfully.')

        self.progress.emit(100, 'Initialisation complete')
        logging.info('Initialisation completed.')

    def terminate(self):
        try:
            kill_subprocess(self.cmd.pid)
        except AttributeError:
            pass
        super().terminate()
