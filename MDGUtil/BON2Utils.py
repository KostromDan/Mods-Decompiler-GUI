import os
import time
from collections import OrderedDict

import jpype

from MDGLogic.InitialisationThread import ExceptionThread
from MDGUtil import PathUtils

DEFAULT_MAPPINGS = OrderedDict([('1.15', ['stable_60']),
                                ('1.14.4', ['stable_58']),
                                ('1.14.3', ['stable_56']),
                                ('1.14.2', ['stable_53']),
                                ('1.14.1', ['stable_51']),
                                ('1.14', ['stable_49']),
                                ('1.13.2', ['stable_47']),
                                ('1.13.1', ['stable_45']),
                                ('1.13', ['stable_43', 'stable_42', 'stable_41']),
                                ('1.12', ['stable_39']),
                                ('1.11', ['stable_32', 'stable_31']),
                                ('1.10.2', ['stable_29']),
                                ('1.9.4', ['stable_26']),
                                ('1.9', ['stable_24']),
                                ('1.8.9', ['stable_22']),
                                ('1.8.8', ['stable_20']),
                                ('1.8', ['stable_18', 'stable_17', 'stable_16', 'stable_15']),
                                ('1.7.10', ['stable_12', 'stable_11', 'stable_10', 'stable_9', 'stable_8'])])


def get_cmp_key(version: str) -> list[int]:
    return list(map(int, version.split('.')))


def get_mappings() -> OrderedDict[str, list]:
    try:
        jpype.startJVM(jpype.getDefaultJVMPath())
        jpype.addClassPath(os.path.abspath(PathUtils.BON2_PATH))
        MappingVersions = jpype.JClass('com.github.parker8283.bon2.util.MappingVersions')
        known_versions_map = MappingVersions.getKnownVersions(True)

        known_versions_dict = {}
        for entry in known_versions_map.entrySet():
            key = str(entry.getKey().toString())

            if get_cmp_key(key) > [1, 16, 5]:
                continue
            value = list(reversed([str(v).removeprefix(f'{key} ').replace(' ', '_')
                                   for v in entry.getValue() if
                                   not any(e in str(v) for e in ['snapshot', 'official'])]))
            if not value:
                continue
            known_versions_dict[key] = value

        sorted_dict = OrderedDict(sorted(known_versions_dict.items(), key=lambda x: get_cmp_key(x[0]), reverse=True))

        return sorted_dict

    except BaseException as e:
        thread = ExceptionThread(e)
        thread.start()
        thread.wait()
        return OrderedDict()  # Empty ordered dictionary
    finally:
        jpype.shutdownJVM()
