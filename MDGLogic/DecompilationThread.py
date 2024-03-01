import logging

from MDGLogic.AbstractMDGThread import AbstractMDGThread


class DecompilationThread(AbstractMDGThread):
    def run(self):
        if not self.serialized_widgets['deobf_check_box']['isChecked']:
            self.progress.emit(100, "Deobfuscation skipped.")
            logging.info("Deobfuscation skipped.")
            return

        logging.info('Started deobfuscation.')

        self.progress.emit(100, "Deobfuscation complete.")
