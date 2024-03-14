import logging
import os
import shutil

from PySide6.QtCore import Signal

from MDGLogic.AbstractMDGThread import AbstractMDGThread
from MDGUtil import FileUtils
from MDGUtil import PathUtils


class CopyThread(AbstractMDGThread):
    use_cached_signal = Signal(object)

    def run(self) -> None:
        mods_path = self.serialized_widgets['mods_path_line_edit']['text']
        cache_enabled = self.serialized_widgets['cache_check_box']['isChecked']
        self.progress.emit(0, 'Starting copying mods')

        jar_in_jar_mods_list = []
        if self.serialized_widgets['jar_in_jar_check_box']['isChecked']:
            logging.info('Started analysing mods for jar in jar.')
            for mod in os.listdir(mods_path):
                FileUtils.extract_jars_from_jar(os.path.join(mods_path, mod), PathUtils.TMP_MODS_PATH)
            jar_in_jar_mods_list += os.listdir(PathUtils.TMP_MODS_PATH)
            logging.info('Finished analysing mods for jar in jar.'
                         f'Found and extracted: {len(jar_in_jar_mods_list)}.')

        mods_list = list(filter(lambda x: x.endswith('.jar'), os.listdir(mods_path)))
        mods_list += jar_in_jar_mods_list  # add jar in jar
        mods_list_without_space = [mod.replace(' ', '_') for mod in mods_list]
        mods_count = len(mods_list)
        logging.info(f'Found in mods folder files with .jar extension: {mods_count}')
        FileUtils.create_folder(PathUtils.TMP_MODS_PATH)
        use_cached_decomp = []
        use_cached_deobf = []
        if cache_enabled:
            try:  # remove mods from decompiled_mods which not in current mods_list
                for mod in os.listdir(PathUtils.DECOMPILED_MODS_PATH):
                    path_to_mod = os.path.join(PathUtils.DECOMPILED_MODS_PATH, mod)
                    if os.path.isfile(path_to_mod):
                        continue
                    mod_name = mod.removesuffix('_mapped_official') + '.jar'
                    decompiled_with_deobf = '_mapped_official' in mod
                    deobf_enabled = self.serialized_widgets['deobf_check_box']['isChecked']
                    if (mod_name in mods_list_without_space and ((decompiled_with_deobf and deobf_enabled) or
                                                                 (not decompiled_with_deobf and not deobf_enabled))):
                        use_cached_decomp.append(mod_name)
                        logging.info(f'Found {mod_name} in decompiled_mods. Coping skipped.')
                    else:
                        shutil.rmtree(path_to_mod)
                        logging.info(f'Found {mod_name} in decompiled_mods.'
                                     f"Current mod list doesn't include it. Removing.")
            except FileNotFoundError:
                pass
            # try:  # remove mods from deobfuscated_mods which in decompiled_mods
            #     for mod in os.listdir(PathUtils.DEOBFUSCATED_MODS_PATH):
            #         mod_name = mod.removesuffix('.jar').removesuffix('_mapped_official') + '.jar'
            #         if mod_name in use_cached:
            #             os.remove(os.path.join(os.path.join(PathUtils.DEOBFUSCATED_MODS_PATH, mod)))
            #             logging.info(f'Removed {mod_name} from deobuscated mods, '
            #                          f'since it already in decompilated mods cache.')
            # except FileNotFoundError:
            #     pass
            try:  # remove mods from deobfuscated_mods which not in current mods_list
                for mod in os.listdir(PathUtils.DEOBFUSCATED_MODS_PATH):
                    mod_name = mod.removesuffix('.jar').removesuffix('_mapped_official') + '.jar'
                    if mod_name in mods_list_without_space:
                        use_cached_deobf.append(mod_name)
                        logging.info(f'Found {mod_name} in deobfuscated mods. Coping skipped.')
                    else:
                        os.remove(os.path.join(PathUtils.DEOBFUSCATED_MODS_PATH, mod))
                        logging.info(f'Found {mod_name} in deobfuscated mods.'
                                     f"Current mod list doesn't include it. Removing.")
            except FileNotFoundError:
                pass
        self.use_cached_signal.emit(use_cached_decomp)

        for mod in jar_in_jar_mods_list:
            if mod in use_cached_deobf:
                os.remove(os.path.join(PathUtils.TMP_MODS_PATH, mod))

        for i, mod in enumerate(mods_list):
            if mod.replace(' ', '_') in use_cached_deobf or mod in jar_in_jar_mods_list:
                continue
            mod_path = os.path.join(mods_path, mod)
            self.progress.emit(int((i / mods_count) * 100), f'Copying {mod}')
            logging.info(f'Starting copying {mod}')
            shutil.copy(mod_path, PathUtils.TMP_MODS_PATH)
            if ' ' in mod:
                os.rename(os.path.join(PathUtils.TMP_MODS_PATH, mod),
                          os.path.join(PathUtils.TMP_MODS_PATH, mod.replace(' ', '_')))
            logging.info(f'Finished copying {mod}')

        self.progress.emit(100, 'Finished copying mods.')
