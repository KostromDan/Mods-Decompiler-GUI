import logging
import os
import zipfile

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil.FileUtils import create_folder

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


def unzip_and_patch_mdk(mdk_path, unzip_to_path, deobf_to_folder_name, do_pacth):
    zipfile.ZipFile(mdk_path).extractall(path=unzip_to_path)
    if do_pacth:
        with open(os.path.join(unzip_to_path, 'build.gradle'), 'a') as file:
            file.write(MDK_PATCH_STRING.replace('local_MDG', deobf_to_folder_name))
        create_folder(os.path.join(unzip_to_path, 'libs'))


class MdkInitialisationThread(AbstractMDGThread):
    def run(self):
        if not self.serialized_widgets['mdk_path_line_edit']['isEnabled']:
            self.progress.emit(100, "Initialisation of mdk skipped.")
            logging.info("Initialisation of mdk skipped.")
            return

        mdk_path = self.serialized_widgets['mdk_path_line_edit']['text']

        self.progress.emit(10, "Unzipping and patching mdk.")
        logging.info('Started unzipping and patching mdk.')
        unzip_and_patch_mdk(mdk_path, 'tmp/mdk', 'local_MDG',False)
        logging.info('Finished unzipping and patching mdk.')

        self.progress.emit(30, "Started initialisation of mdk.")
        logging.info("Started initialisation of mdk.")
        logging.warning(f'If you initializing mdk of this version first time on you pc, it can take some time.')
        os.system("cd tmp/mdk && .\gradlew.bat build")
        logging.info("Finished initialisation of mdk.")

        self.progress.emit(100, "Initialisation of mdk complete.")
