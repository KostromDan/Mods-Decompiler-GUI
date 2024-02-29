import logging
import os
import sys
from datetime import datetime

from PySide6.QtCore import QObject, Signal

from MDGUtil.FileUtils import create_folder, remove_folder

LOGGER_FORMAT = "[%(asctime)s] [%(levelname)s]: %(message)s"
LOGGER_WIDGET_COLORS = {
    'INFO': 'black',
    'WARNING': 'orange',
    'CRITICAL': 'red'
}


class RelativePathFilter(logging.Filter):
    def filter(self, record):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        record.relativepath = os.path.relpath(record.pathname, project_root)
        return True


class LoggerSignal(QObject):
    append_logger_signal = Signal(str, str)

    def append_logger(self, color, msg):
        self.append_logger_signal.emit(color, msg)


class PySideHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        msg = self.format(record)
        MDGLogger().logger_signal.append_logger(LOGGER_WIDGET_COLORS[record.levelname], msg)


class MDGLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
        else:
            return

        if getattr(sys, 'frozen', True) and not hasattr(sys, '_MEIPASS'):  # not inside pyinstaller
            remove_folder('logs')

        self.logger_signal = LoggerSignal()

        create_folder('logs')

        logging.basicConfig(level=logging.INFO, filename=os.path.join('logs', self.get_log_name()),
                            filemode="w",
                            format=LOGGER_FORMAT)

        logger = logging.getLogger()
        logger.addFilter(RelativePathFilter())

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(LOGGER_FORMAT))
        logger.addHandler(console_handler)

        pyside_handler = PySideHandler()
        pyside_handler.setFormatter(logging.Formatter(LOGGER_FORMAT))
        logger.addHandler(pyside_handler)

        logging.info("Logger initialisation complete.")

    def get_log_name(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        current_date_count = 0
        for file in os.listdir('logs'):
            if file.startswith(current_date):
                current_date_count += 1
        return f'{current_date}-{current_date_count}'
