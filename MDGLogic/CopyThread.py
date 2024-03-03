import logging
import os
import shutil

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil.FileUtils import create_folder


class CopyThread(AbstractMDGThread):
    def run(self):
        mods_path = self.serialized_widgets['mods_path_line_edit']['text']
        self.progress.emit(0, 'Starting copying mods')
        mods_list = list(filter(lambda x: x.endswith('.jar'), os.listdir(mods_path)))
        mods_count = len(mods_list)
        logging.info(f'Found in mods folder files with .jar extension: {mods_count}')
        copy_to = 'tmp/mods'
        create_folder(copy_to)
        for i, mod in enumerate(mods_list, start=0):
            mod_path = os.path.join(mods_path, mod)
            self.progress.emit(int((i / mods_count) * 100), f'Copying {mod}')
            logging.info(f'Starting copying {mod}')
            shutil.copy(mod_path, copy_to)
            if ' ' in mod:
                os.rename(os.path.join('tmp', 'mods', mod), os.path.join('tmp', 'mods', mod.replace(' ', '_')))
            logging.info(f'Finished copying {mod}')
        self.progress.emit(100, 'Finished copying mods.')
