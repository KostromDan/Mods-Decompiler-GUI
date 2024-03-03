import logging
import os
import subprocess
import zipfile

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil.FileUtils import create_folder
from MDGUtil.SubprocessKiller import kill_subprocess

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


def patch_mdk_download_sources(mdk_path):
    with open(os.path.join(mdk_path, 'build.gradle'), 'a') as file:
        file.write(MDK_PATCH_STRING_DOWNLOAD_SOURCES)
    create_folder(os.path.join(mdk_path, 'libs'))


def patch_mdk_deobf(mdk_path, deobf_to_folder_name):
    with open(os.path.join(mdk_path, 'build.gradle'), 'a') as file:
        file.write(MDK_PATCH_STRING_DEOBF.replace('local_MDG', deobf_to_folder_name))
    create_folder(os.path.join(mdk_path, 'libs'))


def unzip_and_patch_mdk(mdk_path, unzip_to_path, deobf_to_folder_name, do_deobf_patch, do_download_sources_patch=False):
    zipfile.ZipFile(mdk_path).extractall(path=unzip_to_path)
    if do_deobf_patch:
        patch_mdk_deobf(unzip_to_path, deobf_to_folder_name)
    if do_download_sources_patch:
        patch_mdk_download_sources(unzip_to_path)


class MdkInitialisationThread(AbstractMDGThread):
    def run(self):
        if not self.serialized_widgets['mdk_path_line_edit']['isEnabled']:
            self.progress.emit(100, "Initialisation of mdk skipped.")
            logging.info("Initialisation of mdk skipped.")
            return

        mdk_path = self.serialized_widgets['mdk_path_line_edit']['text']
        do_path_download_sources = (self.serialized_widgets['download_sources_check_box']['isEnabled'] and
                                    self.serialized_widgets['download_sources_check_box']['isChecked'])

        self.progress.emit(10, "Unzipping and patching mdk.")
        logging.info('Started unzipping and patching mdk.')
        unzip_and_patch_mdk(mdk_path, 'result/merged_mdk', 'local_MDG', False, do_path_download_sources)
        logging.info('Finished unzipping and patching mdk.')

        self.progress.emit(30, "Started initialisation of mdk.")
        logging.info("Started initialisation of mdk.")
        logging.warning(f'If you initializing mdk of this version first time on you pc, it can take some time.')
        self.cmd = subprocess.Popen(["gradlew.bat", "build"], cwd=os.path.join('result', 'merged_mdk'), shell=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = self.cmd.communicate()
        if 'BUILD SUCCESSFUL' not in out.decode():
            if 'Could not determine java version from' in err.decode():
                self.critical_signal.emit('Wrong java version',
                                          'MDK init failed due to wrong java version.\n'
                                          'Check what your java version is fit for this MDK.')
            else:
                self.critical_signal.emit('MDK init failed', 'MDK init failed.')

        logging.info("Finished initialisation of mdk.")

        self.progress.emit(100, "Initialisation of mdk complete.")

    def terminate(self):
        try:
            kill_subprocess(self.cmd.pid)
        except AttributeError:
            pass
        super().terminate()
