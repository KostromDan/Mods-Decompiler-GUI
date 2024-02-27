import json
import os
import shutil


class LocalConfig:
    config = dict()
    config_path = os.path.join("local", "config.json")

    def __init__(self):
        self.load()

    def load(self):
        try:
            with open(self.config_path, "r") as file:
                self.config = json.loads(file.read())
        except FileNotFoundError:
            self.save()

    def save(self):
        try:
            os.mkdir("local")
        except FileExistsError:
            pass
        with open(self.config_path, "w") as file:
            file.write(json.dumps(self.config))

    def is_first_launch(self):
        if "launched" not in self.config:
            self.config["launched"] = True
            self.save()
            return True
        return False

    def get(self, arg):
        return self.config.get(arg, "")

    def set(self, arg, value):
        self.config[arg] = value
        self.save()
