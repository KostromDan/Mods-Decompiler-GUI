import json
import logging
import os
import shutil
import subprocess
import time

from PySide6.QtCore import QThread

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil import FileUtils
from MDGUtil.FileUtils import create_folder, remove_folder
from MDGUtil.SubprocessKiller import kill_subprocess
from MDGUtil.SubprocessOutsAnalyseThread import SubprocessOutsAnalyseThread


class ExceptionThread(QThread):
    def __init__(self, e):
        super().__init__()
        self.e = e

    def run(self):
        raise self.e


class InitialisationThread(AbstractMDGThread):
    def run(self):
        decomp_cmd = self.serialized_widgets['decomp_cmd_line_edit']['text']
        cache_enabled = self.serialized_widgets['cache_check_box']['isChecked']

        self.progress.emit(20, 'Clearing tmp folder')
        FileUtils.clear_tmp_folders()
        logging.info('Cleared tmp folders.')

        self.progress.emit(40, 'Clearing result folder')
        if cache_enabled:
            create_folder('result')
            if not self.serialized_widgets['deobf_check_box']['isChecked']:
                remove_folder(os.path.join('result', 'deobfuscated_mods'))
            if not self.serialized_widgets['decomp_check_box']['isChecked']:
                remove_folder(os.path.join('result', 'decompiled_mods'))
            for file in os.listdir('result'):  # remove all except ['deobfuscated_mods', 'decompiled_mods']
                path = os.path.join('result', file)
                if file not in ['deobfuscated_mods', 'decompiled_mods']:
                    if os.path.isfile(path):
                        os.remove(path)
                    else:
                        logging.info(f'Clearing {file}')
                        shutil.rmtree(path)

            cache_path = os.path.join('result', 'decompiled_mods', 'cache.json')
            if not os.path.exists(cache_path):
                remove_folder(os.path.join('result', 'decompiled_mods'))
            try:  # remove mods decompilation of which was interrupted
                with open(cache_path, 'r') as f:
                    cache = json.loads(f.read())
                for mod in os.listdir(os.path.join('result', 'decompiled_mods')):
                    mod_path = os.path.join('result', 'decompiled_mods', mod)
                    if mod not in cache and os.path.isdir(mod_path):
                        shutil.rmtree(mod_path)
                        logging.info(f'Found {mod} in decompiled mods.'
                                     f'But it\'s not in cache. Removing. '
                                     f'Maybe decompilation of it was interrupted.')
            except FileNotFoundError:
                pass

        else:
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
                self.cmd = subprocess.Popen(decomp_cmd_formatted, shell=True,
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
