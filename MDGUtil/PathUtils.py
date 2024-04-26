import locale
import os
import platform
import re
import subprocess
import sys
from pathlib import Path

import win32com.client
import winshell

from MDGUtil.MDGLogger import MDGLogger

MINECRAFT_FORGE_DOWNLOADS_PAGE = 'https://files.minecraftforge.net/net/minecraftforge/forge/'
ADOPTIUM_DOWNLOADS_PAGE = ('https://adoptium.net/temurin/releases/'
                           f"?version=18&package=jdk&arch=x{platform.architecture()[0].removesuffix('bit')}")

java_homes = None


def get_gradle_caches_path():
    gradle_user_home = os.environ.get('GRADLE_USER_HOME')

    if gradle_user_home:
        gradle_caches_path = os.path.join(gradle_user_home, 'caches')
    else:
        home_dir = os.path.expanduser('~')
        gradle_caches_path = os.path.join(home_dir, '.gradle', 'caches')

    return gradle_caches_path


FORGE_GRADLE_DEOBF_CACHE_FOLDER = os.path.join(get_gradle_caches_path(),
                                               'forge_gradle',
                                               'deobf_dependencies')

DECOMPILER_FOLDER_PATH = os.path.join('decompiler')
TEST_MOD_PATH = os.path.join(DECOMPILER_FOLDER_PATH, 'test-mod.jar')
DECOMPILER_JAR_PATH = os.path.join(DECOMPILER_FOLDER_PATH, 'vineflower-1.10.1.jar')
BON2_PATH = os.path.join(DECOMPILER_FOLDER_PATH, 'BON2-2.5.1-CUSTOM-all.jar')

TMP_FOLDER_PATH = os.path.join('tmp')
TMP_MODS_HASHES_PATH = os.path.join(TMP_FOLDER_PATH, 'mods_hashes.json')
TMP_MODS_PATH = os.path.join(TMP_FOLDER_PATH, 'mods')
TMP_DECOMPILER_TEST_PATH = os.path.join(TMP_FOLDER_PATH, 'decompiler_test')
TMP_BON2_TEST_PATH = os.path.join(TMP_FOLDER_PATH, 'bon2_test')
TMP_DEOBFUSCATION_MDKS_PATH = os.path.join(TMP_FOLDER_PATH, 'deobfuscation_MDKs')
TMP_DEOBFUSCATION_BON2_PATH = os.path.join(TMP_FOLDER_PATH, 'deobfuscation_bon2')

RESULT_FOLDER_PATH = os.path.join('result')
DEOBFUSCATED_MODS_PATH = os.path.join(RESULT_FOLDER_PATH, 'deobfuscated_mods')
DEOBFUSCATED_CACHE_PATH = os.path.join(DEOBFUSCATED_MODS_PATH, 'cache.json')
DECOMPILED_MODS_PATH = os.path.join(RESULT_FOLDER_PATH, 'decompiled_mods')
DECOMPILED_CACHE_PATH = os.path.join(DECOMPILED_MODS_PATH, 'cache.json')
MERGED_MDK_PATH = os.path.join(RESULT_FOLDER_PATH, 'merged_mdk')
VINEFLOWER_ISSUES = os.path.join(RESULT_FOLDER_PATH, 'vineflower_issues')
VINEFLOWER_ISSUE_TEMPLATE = os.path.join(DECOMPILER_FOLDER_PATH, 'issue_template.md')

MERGED_MDK_SRC_PATH = os.path.join(MERGED_MDK_PATH, 'src', 'main')
MERGED_MDK_RESOURCES_PATH = os.path.join(MERGED_MDK_SRC_PATH, 'resources')
MERGED_MDK_JAVA_PATH = os.path.join(MERGED_MDK_SRC_PATH, 'java')

LOGS_FOLDER = os.path.join('logs')

DEFAULT_DECOMPILER_CMD = rf'{{java}} -jar {DECOMPILER_JAR_PATH} -dgs=1 -din=1 -log=WARN {{path_to_jar}} {{out_path}}'
DEFAULT_BON2_CMD = (
    r'{java} -jar {bon2_path} --inputJar {path_to_jar} --outputJar {out_path} --mcVer {mc_ver} '
    r'--mappingsVer {mappings_ver} --notch')


def check_pyinstaller_env() -> bool:
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')


def get_all_java_homes() -> list[str]:
    global java_homes
    if java_homes is not None:
        return java_homes
    java_homes = set()

    """JAVA_HOME"""
    java_home = os.environ.get('JAVA_HOME', '')
    if java_home != '':
        java_homes.add(java_home.rstrip('/\\'))

    """java cmd"""
    try:
        output = subprocess.check_output(['java', '-XshowSettings:properties', '-version'], stderr=subprocess.STDOUT)
        output_lines = output.decode('utf-8', errors='ignore').split('\n')
        for line in output_lines:
            if line.strip().startswith('java.home'):
                java_path = line.split('=', 1)[1].strip().rstrip('/\\')
                java_homes.add(java_path)
    except Exception:
        pass

    """PATH"""
    try:
        paths = os.environ['PATH'].split(os.pathsep)
        for path in paths:
            java_path = os.path.join(path, 'java.exe')
            if os.path.exists(java_path):
                java_home = os.path.dirname(os.path.dirname(java_path))
                java_homes.add(java_home.rstrip('/\\'))
    except KeyError:
        pass

    """ftype"""
    try:
        output = subprocess.check_output(['ftype', ], shell=True, stderr=subprocess.STDOUT)
        output_lines = output.decode('utf-8', errors='ignore').split('\n')
        for line in output_lines:
            line = line.strip()
            line = re.sub(r'[/\\]+', r'\\', line)
            line = line.replace('bin\\javaw.exe', 'bin\\java.exe')
            if 'bin\\java.exe' in line:
                java_path = line.split('=')[1].split('bin\\java.exe')[0].strip('"\\')
                java_homes.add(java_path)
    except Exception:
        pass
    java_homes = list(java_homes)
    return java_homes


def get_all_programs() -> list[str]:
    paths = set()

    """Start Menu/Programs"""
    try:
        programs_paths = {r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs',
                          os.path.join(os.environ['userprofile'], 'Start Menu', 'Programs'),
                          winshell.programs()}
        for programs_path in programs_paths:
            if not os.path.isdir(programs_path):
                continue
            for lnk_path in Path(programs_path).rglob('*.lnk'):
                shell = win32com.client.Dispatch('WScript.Shell')
                shortcut = shell.CreateShortCut(str(lnk_path))
                paths.add(shortcut.Targetpath)
    except Exception:
        pass

    """wmic"""
    try:
        p = subprocess.Popen(['wmic', 'process', 'get', 'executablepath'], shell=True, stdout=subprocess.PIPE, )
        stdout = p.communicate()[0].decode(locale.getpreferredencoding())
        arr = [i.strip() for i in stdout.split('\n') if i.strip() not in ['ExecutablePath', '']]
        for i in arr:
            paths.add(i)
    except Exception:
        pass

    return list(paths)


def get_eclipse_paths() -> list[str]:
    return list(filter(lambda p: p.endswith('eclipse.exe'), get_all_programs()))


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
                              out_path: str | os.PathLike) -> str:
    return cmd.format(java=get_path_to_java(java_home),
                      path_to_jar=path_to_jar,
                      out_path=out_path)


def format_bon2_command(cmd: str,
                        java_home: str | os.PathLike,
                        bon2_path: str | os.PathLike,
                        path_to_jar: str | os.PathLike,
                        out_path: str | os.PathLike,
                        version: str,
                        mappings: str) -> str:
    return cmd.format(java=get_path_to_java(java_home),
                      bon2_path=f'"{os.path.abspath(bon2_path)}"',
                      path_to_jar=f'"{os.path.abspath(path_to_jar)}"',
                      out_path=f'"{os.path.abspath(out_path)}"',
                      mc_ver=version,
                      mappings_ver=mappings)


def open_log():
    os.startfile(MDGLogger().get_path_to_log())
