import os.path
import shutil
import threading

from MDGLogic.MdkInitialisationThread import unzip_and_patch_mdk
from MDGUtil.FileUtils import create_folder


class DeobfuscationThread(threading.Thread):

    def __init__(self, mod_path: str, thread_number: int, serialized_widgets: dict):
        self.mod_path = mod_path
        self.thread_number = thread_number
        self.serialized_widgets = serialized_widgets
        self.success = False
        super().__init__()

    def run(self):
        create_folder('deobfuscation_MDKs')
        current_mdk_path = f'tmp/deobfuscation_MDKs/mdk_{self.thread_number}'
        deobfed_folder_name = f'local_MDG_{self.thread_number}'
        unzip_and_patch_mdk(self.serialized_widgets['mdk_path_line_edit']['text'],
                            current_mdk_path,
                            deobfed_folder_name,
                            True)
        shutil.copy(self.mod_path, os.path.join(current_mdk_path, 'libs'))
        os.system(f"cd {current_mdk_path} && .\gradlew.bat build")
        deobfed_mods_path = os.path.join(os.path.expanduser('~'),
                                         '.gradle',
                                         'caches',
                                         'forge_gradle',
                                         'deobf_dependencies',
                                         deobfed_folder_name)
        if not os.path.exists(deobfed_mods_path):
            self.success = False
            return

        create_folder('result/deobfuscated_mods')
        for mod_dir in os.listdir(deobfed_mods_path):
            dir_2 = os.path.join(deobfed_mods_path, mod_dir)
            jar_dir = os.path.join(dir_2, os.listdir(dir_2)[0])
            for file in os.listdir(jar_dir):
                if file.endswith('.jar'):
                    path_to_jar = os.path.join(jar_dir, file)
                    mod_original_name = os.path.basename(self.mod_path)
                    mod_mapped_name = os.path.basename(path_to_jar)
                    mod_new_mapped_name = mod_original_name.rstrip('.jar') + '_mapped_official.jar'
                    new_jar_path = os.path.join(os.path.dirname(path_to_jar), mod_new_mapped_name)
                    try:
                        os.rename(path_to_jar,
                                  new_jar_path)
                    except FileExistsError:
                        pass
                    shutil.copy(new_jar_path, 'result/deobfuscated_mods')
                    break
        self.success = True

    def terminate(self):
        pass
