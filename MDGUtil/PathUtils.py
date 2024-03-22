import os
import sys

MINECRAFT_FORGE_DOWNLOADS_PAGE = 'https://files.minecraftforge.net/net/minecraftforge/forge/'

FORGE_GRADLE_DEOBF_CACHE_FOLDER = os.path.join(os.path.expanduser('~'),
                                               '.gradle',
                                               'caches',
                                               'forge_gradle',
                                               'deobf_dependencies')

DECOMPILER_FOLDER_PATH = os.path.join('decompiler')
TEST_MOD_PATH = os.path.join(DECOMPILER_FOLDER_PATH, 'decompiler_test_mod.jar')
DECOMPILER_JAR_PATH = os.path.join(DECOMPILER_FOLDER_PATH, 'vineflower-1.10.0+local.jar')
BON2_PATH = os.path.join(DECOMPILER_FOLDER_PATH, 'BON2-2.5.1-CUSTOM-all.jar')

TMP_FOLDER_PATH = os.path.join('tmp')
TMP_MODS_PATH = os.path.join(TMP_FOLDER_PATH, 'mods')
TMP_DECOMPILER_TEST_PATH = os.path.join(TMP_FOLDER_PATH, 'decompiler_test')
TMP_DEOBFUSCATION_MDKS_PATH = os.path.join(TMP_FOLDER_PATH, 'deobfuscation_MDKs')

RESULT_FOLDER_PATH = os.path.join('result')
DEOBFUSCATED_MODS_PATH = os.path.join(RESULT_FOLDER_PATH, 'deobfuscated_mods')
DECOMPILED_MODS_PATH = os.path.join(RESULT_FOLDER_PATH, 'decompiled_mods')
MERGED_MDK_PATH = os.path.join(RESULT_FOLDER_PATH, 'merged_mdk')

MERGED_MDK_SRC_PATH = os.path.join(MERGED_MDK_PATH, 'src', 'main')
MERGED_MDK_RESOURCES_PATH = os.path.join(MERGED_MDK_SRC_PATH, 'resources')
MERGED_MDK_JAVA_PATH = os.path.join(MERGED_MDK_SRC_PATH, 'java')

DEFAULT_DECOMPILER_CMD = rf'{{java}} -jar {DECOMPILER_JAR_PATH} -dgs=1 -din=1 {{path_to_jar}} {{out_path}}'
DEFAULT_BON2_CMD = (rf'{{java}} -jar {BON2_PATH} --inputJar {{path_to_jar}} --outputJar {{out_path}} --mcVer {{mc_ver}} '
                    rf'--mappingsVer {{mappings_ver}} --notch')


def check_pyinstaller_env() -> bool:
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')


def get_java_home_from_env() -> str:
    return os.environ.get('JAVA_HOME', '')
