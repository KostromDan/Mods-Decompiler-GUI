import os
import platform
import sys

MINECRAFT_FORGE_DOWNLOADS_PAGE = 'https://files.minecraftforge.net/net/minecraftforge/forge/'
ADOPTIUM_DOWNLOADS_PAGE = ('https://adoptium.net/temurin/releases/'
                           f'?version=18&package=jdk&arch=x{platform.architecture()[0].removesuffix('bit')}')

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
DEFAULT_BON2_CMD = (
    rf'{{java}} -jar {BON2_PATH} --inputJar {{path_to_jar}} --outputJar {{out_path}} --mcVer {{mc_ver}} '
    rf'--mappingsVer {{mappings_ver}} --notch')


def check_pyinstaller_env() -> bool:
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')


def get_all_java_homes() -> list[str]:
    java_homes = list()
    java_home = os.environ.get('JAVA_HOME', '')
    if java_home != '':
        java_homes.append(java_home)
    try:
        paths = os.environ['PATH'].split(os.pathsep)
        for path in paths:
            java_path = os.path.join(path, 'java.exe')
            if os.path.exists(java_path):
                java_home = os.path.dirname(os.path.dirname(java_path))
                if java_home not in java_homes:
                    java_homes.append(java_home)
    except KeyError:
        pass
    return java_homes


def get_java_home() -> str:
    java_homes = get_all_java_homes()
    return java_homes[0] if java_homes else ''


def get_path_to_java(java_home: str) -> str:
    java = os.path.join(java_home, 'bin', 'java')
    if os.path.exists(java):
        return f'"{java}"'
    java += '.exe'
    if os.path.exists(java):
        return f'"{java}"'
    raise FileNotFoundError("Can't find JVM in provided path!")


def get_env_with_patched_java_home(java_home: str) -> dict[str, str]:
    env = os.environ.copy()
    env['JAVA_HOME'] = java_home
    return env


def format_decompiler_command(cmd: str,
                              java_home: str | os.PathLike,
                              path_to_jar: str | os.PathLike,
                              out_path: str | os.PathLike, ) -> str:
    return cmd.format(java=get_path_to_java(java_home), path_to_jar=path_to_jar, out_path=out_path)
