from  MDGUtil import FileUtils
from MDGLogic.AbstractMDGThread import AbstractMDGThread


class InitThread(AbstractMDGThread):
    def run(self):
        self.progress.emit(10, "Clearing tmp folders")
        FileUtils.clear_tmp_folders()
        self.progress.emit(40, "Clearing result folders")
        FileUtils.clear_result_folders()
        self.progress.emit(70, "Creating new folders")
        FileUtils.init_folders()
        self.progress.emit(100, "Initialisation complete")
