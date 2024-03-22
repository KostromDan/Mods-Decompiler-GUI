import logging
import os
import subprocess
import sys
import zipfile

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil import PathUtils, FileUtils
from MDGUtil.SubprocessKiller import kill_subprocess
from MDGUtil.SubprocessOutsAnalyseThread import SubprocessOutsAnalyseThread

MDK_PATCH_STRING_DEOBF = """repositories {
    flatDir {
        dir 'libs'
    }
}
dependencies {
    fileTree(include: ['*.jar'], dir: 'libs').each { file ->
        def fileNameWithoutDotJarExtension = file.name.substring(0, file.name.length() - 4)
        def indexOfLastDash = fileNameWithoutDotJarExtension.lastIndexOf('-');
        project.logger.warn("starting deobfuscating ${file.name}")
        implementation fg.deobf("local_MDG:${fileNameWithoutDotJarExtension.substring(0, indexOfLastDash)}:${fileNameWithoutDotJarExtension.substring(indexOfLastDash + 1)}")
    }
}"""
MDK_PATCH_STRING_DOWNLOAD_SOURCES = """apply plugin: 'idea'
idea {
    module {
        downloadSources = true
    }
}

apply plugin: 'eclipse'
eclipse {
    classpath {
        downloadSources = true
    }
}
"""


def patch_mdk_download_sources(mdk_path: str | os.PathLike) -> None:
    with open(os.path.join(mdk_path, 'build.gradle'), 'a') as file:
        file.write(MDK_PATCH_STRING_DOWNLOAD_SOURCES)
    FileUtils.create_folder(os.path.join(mdk_path, 'libs'))


def patch_mdk_deobf(mdk_path: str | os.PathLike,
                    deobf_to_folder_name: str) -> None:
    with open(os.path.join(mdk_path, 'build.gradle'), 'a') as file:
        file.write(MDK_PATCH_STRING_DEOBF.replace('local_MDG', deobf_to_folder_name))
    FileUtils.create_folder(os.path.join(mdk_path, 'libs'))


def unzip_and_patch_mdk(mdk_path: str | os.PathLike,
                        unzip_to_path: str | os.PathLike,
                        deobf_to_folder_name: str,
                        do_deobf_patch: bool,
                        do_download_sources_patch: bool = False) -> None:
    zipfile.ZipFile(mdk_path).extractall(path=unzip_to_path)
    if do_deobf_patch:
        patch_mdk_deobf(unzip_to_path, deobf_to_folder_name)
    if do_download_sources_patch:
        patch_mdk_download_sources(unzip_to_path)


class MdkInitialisationThread(AbstractMDGThread):
    def run(self) -> None:
        if (not self.serialized_widgets['mdk_path_line_edit']['isEnabled'] or
                (not (self.serialized_widgets['merge_check_box']['isEnabled'] and
                      self.serialized_widgets['merge_check_box']['isChecked']) and
                 len(os.listdir(PathUtils.TMP_MODS_PATH)) == 0)):
            self.progress.emit(100, 'Initialisation of mdk skipped.')
            logging.info('Initialisation of mdk skipped.')
            return

        mdk_path = self.serialized_widgets['mdk_path_line_edit']['text']
        do_path_download_sources = (self.serialized_widgets['download_sources_check_box']['isEnabled'] and
                                    self.serialized_widgets['download_sources_check_box']['isChecked'])

        self.progress.emit(10, 'Unzipping and patching mdk.')
        logging.info('Started unzipping and patching mdk.')
        unzip_and_patch_mdk(mdk_path, PathUtils.MERGED_MDK_PATH, 'local_MDG', False, do_path_download_sources)
        logging.info('Finished unzipping and patching mdk.')

        self.progress.emit(30, 'Started initialisation of mdk.')
        logging.info('Started initialisation of mdk.')
        logging.warning('If you initializing mdk of this version first time on you pc, it can take some time.')
        env = os.environ.copy()
        env['JAVA_HOME'] = self.serialized_widgets['mdk_java_home_line_edit']['text']
        self.cmd = subprocess.Popen(['gradlew.bat', 'compileJava'], cwd=PathUtils.MERGED_MDK_PATH, shell=True,
                                    env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        cmd_out_analyse_thread = SubprocessOutsAnalyseThread(self.cmd, stderr=sys.stdout, err_logger=logging.info)
        cmd_out_analyse_thread.start()
        cmd_out_analyse_thread.join()

        if 'BUILD SUCCESSFUL' not in cmd_out_analyse_thread.out:
            version_errors = ['Could not determine java version from',
                              'java.lang.ExceptionInInitializerError (no error message)']
            if any(error in cmd_out_analyse_thread.err for error in version_errors):
                self.critical_signal.emit('Wrong java version',
                                          'MDK init failed due to wrong JAVA_HOME.\n'
                                          'Try to specify JAVA_HOME that fit for this MDK in '
                                          'JAVA_HOME settings.',
                                          'mdk_java_home_line_edit')
            else:
                self.critical_signal.emit('MDK init failed',
                                          'MDK init failed.\n'
                                          'Check the lastest log for more details.',
                                          None)

        logging.info('Finished initialisation of mdk.')

        self.progress.emit(100, 'Initialisation of mdk complete.')

    def terminate(self) -> None:
        try:
            kill_subprocess(self.cmd.pid)
        except AttributeError:
            pass
        super().terminate()
