import logging
import os
import shutil
import subprocess
import time

from PySide6.QtCore import QThread

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil import FileUtils, PathUtils, UiUtils
from MDGUtil.SubprocessKiller import kill_subprocess
from MDGUtil.SubprocessOutsAnalyseThread import SubprocessOutsAnalyseThread


class ExceptionThread(QThread):
    """
    Class created to raise exception without interrupting process.
    For logging.
    """

    def __init__(self, e: Exception):
        super().__init__()
        self.e = e

    def run(self) -> None:
        raise self.e


class InitialisationThread(AbstractMDGThread):
    def run(self) -> None:
        cache_enabled = self.serialized_widgets['cache_check_box']['isChecked']

        self.progress.emit(20, 'Clearing tmp folder')
        FileUtils.clear_tmp_folders()
        logging.info('Cleared tmp folders.')

        self.progress.emit(40, 'Clearing result folder')
        if cache_enabled:
            FileUtils.create_folder(PathUtils.RESULT_FOLDER_PATH)
            if not self.serialized_widgets['deobf_check_box']['isChecked']:
                FileUtils.remove_folder(PathUtils.DEOBFUSCATED_MODS_PATH)
            if not self.serialized_widgets['decomp_check_box']['isChecked']:
                FileUtils.remove_folder(PathUtils.DECOMPILED_MODS_PATH)
            for file in os.listdir(PathUtils.RESULT_FOLDER_PATH):
                # remove all except ['deobfuscated_mods', 'decompiled_mods']
                path = os.path.join(PathUtils.RESULT_FOLDER_PATH, file)
                if file not in ['deobfuscated_mods', 'decompiled_mods']:
                    if os.path.isfile(path):
                        os.remove(path)
                    else:
                        logging.info(f'Clearing {file}')
                        shutil.rmtree(path)
        else:
            FileUtils.clear_result_folders()
        logging.info('Cleared result folders.')

        self.progress.emit(50, 'Creating new folders')
        FileUtils.init_folders()
        logging.info('Created new folders.')

        if self.serialized_widgets['decomp_cmd_groupbox']['isEnabled']:
            self.progress.emit(80, 'Checking decompiler/decompiler cmd are correct')
            logging.info('Checking decompiler/decompiler cmd are correct')
            FileUtils.create_folder(PathUtils.TMP_DECOMPILER_TEST_PATH)
            cmd_analyse_thread = None
            try:
                decomp_cmd = self.serialized_widgets['decomp_cmd_line_edit']['text']
                java_home = self.serialized_widgets['decompiler_java_home_line_edit']['text']
                decomp_cmd_formatted = (PathUtils.format_decompiler_command(decomp_cmd,
                                                                            java_home,
                                                                            PathUtils.TEST_MOD_PATH,
                                                                            PathUtils.TMP_DECOMPILER_TEST_PATH))

                self.cmd = subprocess.Popen(decomp_cmd_formatted, shell=True,
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                cmd_analyse_thread = SubprocessOutsAnalyseThread(self.cmd)
                cmd_analyse_thread.start()
                cmd_analyse_thread.join()
                assert len(os.listdir(PathUtils.TMP_DECOMPILER_TEST_PATH)) >= 1
            except Exception as e:
                thread = ExceptionThread(e)
                thread.start()
                time.sleep(0.1)
                if cmd_analyse_thread is not None and 'has been compiled by a more recent version of the Java' in cmd_analyse_thread.err:
                    self.critical_signal.emit('Incorrect java version for decompiler',
                                              'This message indicates that decompiler was '
                                              'compiled with more recent version of java '
                                              "than in your JAVA_HOME. Default decompiler uses 17'th version of java. "
                                              'Try to specify path to recent version of java in JAVA_HOME settings.',
                                              'decompiler_java_home_line_edit')
                    return
                self.critical_signal.emit('Incorrect decompiler cmd',
                                          "With this decompiler/decompiler cmd program won't work.\n"
                                          'This message indicates that {path_to_jar} is not decompiled to {out_path}.\n'
                                          'Check decompiler/decompiler cmd: path, syntax, etc. And try again.\n'
                                          'Open the lastest log for more details.\n',
                                          'decomp_cmd_line_edit')
                return
            logging.info('Checked decompiler/decompiler cmd are correct successfully.')
        if UiUtils.is_checked_and_enabled(self.serialized_widgets['deobf_algo_radio_bon2']):
            self.progress.emit(90, 'Checking bon2/bon2 cmd are correct')
            logging.info('Checking bon2/bon2 cmd are correct')
            FileUtils.remove_folder('data')
            FileUtils.remove_folder('--notch')
            FileUtils.create_folder(PathUtils.TMP_BON2_TEST_PATH)
            cmd_analyse_thread = None
            try:
                bon_2_cmd = self.serialized_widgets['bon2_cmd_line_edit']['text']
                java_home = self.serialized_widgets['bon2_java_home_line_edit']['text']
                bon_2_cmd_formatted = (
                    PathUtils.format_bon2_command(bon_2_cmd,
                                                  java_home,
                                                  self.serialized_widgets['bon2_path_line_edit']['text'],
                                                  PathUtils.TEST_MOD_PATH,
                                                  os.path.join(PathUtils.TMP_BON2_TEST_PATH, 'test-mod_mapped.jar'),
                                                  self.serialized_widgets['bon2_version_combo_box']['currentText'],
                                                  self.serialized_widgets['bon2_mappings_combo_box']['currentText']))

                self.cmd = subprocess.Popen(bon_2_cmd_formatted, shell=True,
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                cmd_analyse_thread = SubprocessOutsAnalyseThread(self.cmd)
                cmd_analyse_thread.start()
                cmd_analyse_thread.join()
                FileUtils.remove_folder('data')
                FileUtils.remove_folder('--notch')
                assert len(os.listdir(PathUtils.TMP_BON2_TEST_PATH)) >= 1
                assert cmd_analyse_thread.err == ''
            except Exception as e:
                thread = ExceptionThread(e)
                thread.start()
                time.sleep(0.1)
                if cmd_analyse_thread is not None and 'has been compiled by a more recent version of the Java' in cmd_analyse_thread.err:
                    self.critical_signal.emit('Incorrect java version for bon2',
                                              'This message indicates that bon2 was '
                                              'compiled with more recent version of java '
                                              "than in your JAVA_HOME. Default bon2 uses 17'th version of java. "
                                              'Try to specify path to recent version of java in JAVA_HOME settings.',
                                              'bon2_java_home_line_edit')
                    return
                self.critical_signal.emit('Incorrect bon2 cmd',
                                          "With this bon2/bon2 cmd program won't work.\n"
                                          'This message indicates that {path_to_jar} is not decompiled to {out_path}.\n'
                                          'Check bon2/bon2 cmd: path, syntax, etc. And try again.\n'
                                          'Open the lastest log for more details.\n',
                                          'bon2_cmd_line_edit')
                return
            logging.info('Checked bon2/bon2 cmd are correct')

        self.progress.emit(100, 'Initialisation complete')
        logging.info('Initialisation completed.')

    def terminate(self) -> None:
        try:
            kill_subprocess(self.cmd.pid)
        except AttributeError:
            pass
        super().terminate()
