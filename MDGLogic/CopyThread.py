import hashlib
import json
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

        FileUtils.create_folder(PathUtils.TMP_MODS_PATH)

        mods_list = list(filter(lambda x: x.endswith('.jar'), os.listdir(mods_path)))
        mods_count = len(mods_list)

        for i, mod in enumerate(mods_list):
            mod_path = os.path.join(mods_path, mod)
            self.progress.emit(int((i / mods_count) * 100), f'Copying {mod}')
            logging.info(f'Starting copying {mod}')
            shutil.copy(mod_path, PathUtils.TMP_MODS_PATH)
            try:
                os.rename(os.path.join(PathUtils.TMP_MODS_PATH, mod),
                          os.path.join(PathUtils.TMP_MODS_PATH, FileUtils.remove_unsupported_symbols(mod)))
            except FileExistsError:
                pass
            logging.info(f'Finished copying {mod}')

        self.progress.emit(100, 'Finished copying mods.')
        logging.info(f'Found and copied from mods folder files with .jar extension: {mods_count}')

        if self.serialized_widgets['jar_in_jar_check_box']['isChecked']:
            self.progress.emit(100, 'Analysing mods for jar in jar.')
            logging.info('Started analysing mods for jar in jar.')
            for mod in os.listdir(PathUtils.TMP_MODS_PATH):
                FileUtils.extract_jars_from_jar(os.path.join(PathUtils.TMP_MODS_PATH, mod), PathUtils.TMP_MODS_PATH)
            logging.info('Finished analysing mods for jar in jar. '
                         f'Found and extracted: {len(os.listdir(PathUtils.TMP_MODS_PATH)) - mods_count}.')

        mods_list = os.listdir(PathUtils.TMP_MODS_PATH)
        mods_count = len(mods_list)

        logging.info(f'Total mods count including jar in jar: {mods_count}')

        mod_hashes = dict()
        for mod_name in mods_list:
            mod_path = os.path.join(PathUtils.TMP_MODS_PATH, mod_name)
            mod_hash = hashlib.sha256(open(mod_path, 'rb').read()).hexdigest()
            mod_hashes[mod_name.removesuffix('.jar')] = mod_hash
        with open(PathUtils.TMP_MODS_HASHES_PATH, 'w') as f:
            f.write(json.dumps(mod_hashes))

        if not os.path.exists(PathUtils.DEOBFUSCATED_CACHE_PATH):
            FileUtils.remove_folder(PathUtils.DEOBFUSCATED_MODS_PATH)
        try:  # remove mods deobfuscation of which was interrupted
            with open(PathUtils.DEOBFUSCATED_CACHE_PATH, 'r') as f:
                cache = json.loads(f.read())
            for mod in os.listdir(PathUtils.DEOBFUSCATED_MODS_PATH):
                mod_path = os.path.join(PathUtils.DEOBFUSCATED_MODS_PATH, mod)
                if (mod.removesuffix('.jar').removesuffix('_mapped') not in cache and
                        not os.path.basename(mod_path).endswith('.json')):
                    os.remove(mod_path)
                    logging.info(f'Found {mod} in deobfuscated mods.'
                                 f"But it's not in cache. Removing. "
                                 f'Maybe deobfuscation of it was interrupted.')
        except FileNotFoundError:
            pass

        use_cached_decomp = []
        use_cached_deobf = []
        if cache_enabled:
            if not os.path.exists(PathUtils.DECOMPILED_CACHE_PATH):
                FileUtils.remove_folder(PathUtils.DECOMPILED_MODS_PATH)
            elif os.path.exists(PathUtils.DECOMPILED_MODS_PATH):
                with open(PathUtils.DECOMPILED_CACHE_PATH, 'r') as f:
                    cache = json.loads(f.read())
                for mod in os.listdir(PathUtils.DECOMPILED_MODS_PATH):
                    mod_path = os.path.join(PathUtils.DECOMPILED_MODS_PATH, mod)
                    mod_name_without_jar = mod.removesuffix('.jar').removesuffix('_mapped')
                    mod_name_with_jar = mod_name_without_jar + '.jar'
                    decompiled_with_deobf = '_mapped' in mod
                    deobf_enabled = self.serialized_widgets['deobf_check_box']['isChecked']
                    if mod_name_without_jar.endswith('.json'):
                        continue
                    if mod_name_without_jar not in cache:
                        shutil.rmtree(mod_path)
                        logging.info(f'Found {mod} in decompiled mods.'
                                     f"But it's not in cache. Removing. "
                                     f'Maybe decompilation of it was interrupted.')
                        continue
                    if (mod_name_without_jar in mod_hashes and
                            cache[mod_name_without_jar] != mod_hashes[mod_name_without_jar]):
                        shutil.rmtree(mod_path)
                        logging.info(f'Found {mod} in decompiled mods.'
                                     f'But hash is not same with mod from current mod list. Removing. '
                                     f"Maybe mod changed without changing it's name.")
                        continue
                    if (mod_name_with_jar in mods_list and ((decompiled_with_deobf and deobf_enabled) or
                                                            (not decompiled_with_deobf and not deobf_enabled))):
                        use_cached_decomp.append(mod_name_with_jar)
                    else:
                        shutil.rmtree(mod_path)
                        logging.info(f'Found {mod_name_with_jar} in decompiled_mods. '
                                     f"Current mod list doesn't include it. Removing.")

            if not os.path.exists(PathUtils.DEOBFUSCATED_CACHE_PATH):
                FileUtils.remove_folder(PathUtils.DEOBFUSCATED_MODS_PATH)
            elif os.path.exists(PathUtils.DEOBFUSCATED_MODS_PATH):
                with open(PathUtils.DEOBFUSCATED_CACHE_PATH, 'r') as f:
                    cache = json.loads(f.read())
                for mod in os.listdir(PathUtils.DEOBFUSCATED_MODS_PATH):
                    mod_path = os.path.join(PathUtils.DEOBFUSCATED_MODS_PATH, mod)
                    mod_name_without_jar = mod.removesuffix('.jar').removesuffix('_mapped')
                    mod_name_with_jar = mod_name_without_jar + '.jar'
                    if mod_name_without_jar.endswith('.json'):
                        continue
                    if mod_name_without_jar not in cache:
                        os.remove(mod_path)
                        logging.info(f'Found {mod} in deobfuscated mods.'
                                     f"But it's not in cache. Removing. "
                                     f'Maybe deobfuscation of it was interrupted.')
                        continue
                    if (mod_name_without_jar in mod_hashes and
                            cache[mod_name_without_jar] != mod_hashes[mod_name_without_jar]):
                        os.remove(mod_path)
                        logging.info(f'Found {mod} in deobfuscated mods.'
                                     f'But hash is not same with mod from current mod list. Removing. '
                                     f"Maybe mod changed without changing it's name")
                        continue
                    if mod_name_with_jar in mods_list:
                        use_cached_deobf.append(mod_name_with_jar)
                    else:
                        os.remove(mod_path)
                        logging.info(f'Found {mod_name_with_jar} in deobfuscated mods. '
                                     f"Current mod list doesn't include it. Removing.")

        for mod_name in use_cached_deobf:
            logging.info(f'Found {mod_name} in cache. Removing from tmp folder.')
            os.remove(os.path.join(PathUtils.TMP_MODS_PATH, mod_name))

        self.use_cached_signal.emit(use_cached_decomp)
