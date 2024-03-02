import logging

from MDGLogic.AbstractMDGThread import AbstractMDGThread


class MergingThread(AbstractMDGThread):
    def run(self):
        if not self.serialized_widgets['merge_check_box']['isChecked'] or not \
        self.serialized_widgets['merge_check_box']['isEnabled']:
            self.progress.emit(100, "Merging skipped.")
            logging.info("Merging skipped.")
            return

        logging.info('Merging started.')
        self.progress.emit(0, "Merging started.")

        logging.info('Merging complete.')
        self.progress.emit(100, "Merging complete.")
