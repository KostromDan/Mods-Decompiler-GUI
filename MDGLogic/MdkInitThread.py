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
        implementation fg.deobf("local_mod_source_downloader:${fileNameWithoutDotJarExtension.substring(0, indexOfLastDash)}:${fileNameWithoutDotJarExtension.substring(indexOfLastDash + 1)}")
    }
}"""


class MdkInitThread(AbstractMDGThread):
    def run(self):
        mdk_path = self.serialized_widgets['mdk_path_line_edit']['text']

        self.progress.emit(10, "Unzipping mdk.")
        logging.info('Started unzipping mdk.')
        zipfile.ZipFile(mdk_path).extractall(path='tmp/mdk')
        logging.info('Finished unzipping mdk.')

        self.progress.emit(10, "Patching mdk.")
        with open('tmp/mdk/build.gradle', 'a') as file:
            file.write(MDK_PATCH_STRING)
        create_folder('tmp/mdk/libs')
        logging.info('Patched mdk.')

        self.progress.emit(30, "Started initialisation of mdk.")
        logging.info("Started initialisation of mdk.")
        logging.warning(f'If you initializing mdk of this version first time on you pc, it can take some time.')
        os.system("cd tmp/mdk && .\gradlew.bat build")
        logging.info("Finished initialisation of mdk.")

        self.progress.emit(100, "Initialisation of mdk complete.")
