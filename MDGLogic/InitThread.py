import MDGUtil.FileUtils as file_utils
from MDGLogic.AbstractMDGThread import AbstractMDGThread


class InitThread(AbstractMDGThread):
    def run(self):
        self.progress_window.set_progress(10, "Clearing tmp folders")
        file_utils.clear_tmp_folders()
        self.progress_window.set_progress(40, "Clearing result folders")
        file_utils.clear_result_folders()
        self.progress_window.set_progress(70, "Creating new folders")
        file_utils.init_folders()
        self.progress_window.set_progress(100, "Initialisation complete")
