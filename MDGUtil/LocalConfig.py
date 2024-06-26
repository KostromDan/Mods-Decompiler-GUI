import json
import os
from typing import Any

from built_to_exe import VERSION


class LocalConfig:
    config = dict()
    config_path = os.path.join('local', 'config.json')

    def __init__(self) -> None:
        self.load()

    def load(self) -> None:
        try:
            with open(self.config_path, 'r') as file:
                self.config = json.loads(file.read())
                self.config['last_launch_version'] = VERSION
        except FileNotFoundError:
            self.save()

    def save(self) -> None:
        try:
            os.mkdir('local')
        except FileExistsError:
            pass
        with open(self.config_path, 'w') as file:
            file.write(json.dumps(self.config))

    def is_first_launch(self) -> bool:
        if 'launched' not in self.config:
            self.config['launched'] = True
            self.config['first_launch_version'] = VERSION
            self.save()
            return True
        return False

    def get(self, arg: str) -> Any:
        return self.config.get(arg, '')

    def set(self, arg: str, value: Any) -> None:
        self.config[arg] = value
        self.save()

    def reset(self):
        self.config = dict()
        self.save()
