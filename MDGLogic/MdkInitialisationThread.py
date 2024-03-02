import logging
import os
import subprocess
import zipfile

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil.FileUtils import create_folder
from MDGUtil.SubprocessKiller import kill_subprocess

MDK_PATCH_STRING = """repositories {
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


def patch_mdk(mdk_path, deobf_to_folder_name):
    with open(os.path.join(mdk_path, 'build.gradle'), 'a') as file:
        file.write(MDK_PATCH_STRING.replace('local_MDG', deobf_to_folder_name))
    create_folder(os.path.join(mdk_path, 'libs'))


def unzip_and_patch_mdk(mdk_path, unzip_to_path, deobf_to_folder_name, do_patch):
    zipfile.ZipFile(mdk_path).extractall(path=unzip_to_path)
    if do_patch:
        patch_mdk(unzip_to_path, deobf_to_folder_name)


class MdkInitialisationThread(AbstractMDGThread):
    def run(self):
        if not self.serialized_widgets['mdk_path_line_edit']['isEnabled']:
            self.progress.emit(100, "Initialisation of mdk skipped.")
            logging.info("Initialisation of mdk skipped.")
            return

        mdk_path = self.serialized_widgets['mdk_path_line_edit']['text']

        self.progress.emit(10, "Unzipping and patching mdk.")
        logging.info('Started unzipping and patching mdk.')
        unzip_and_patch_mdk(mdk_path, 'result/merged_mdk', 'local_MDG', False)
        logging.info('Finished unzipping and patching mdk.')

        self.progress.emit(30, "Started initialisation of mdk.")
        logging.info("Started initialisation of mdk.")
        logging.warning(f'If you initializing mdk of this version first time on you pc, it can take some time.')
        self.cmd = subprocess.Popen(["gradlew.bat", "build"], cwd=os.path.join('result', 'merged_mdk'), shell=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = self.cmd.communicate()
        exitcode = self.cmd.returncode
        self.cmd.wait()
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
