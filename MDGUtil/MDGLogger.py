import logging
import os
import sys
import traceback
from datetime import datetime
from types import TracebackType
from typing import Type

from PySide6.QtCore import QObject, Signal

from MDGUtil import FileUtils, PathUtils

LOGGER_FORMAT = '[%(asctime)s] [%(levelname)s]: %(message)s'
LOGGER_WIDGET_COLORS = {
    'INFO': 'black',
    'WARNING': 'orange',
    'CRITICAL': 'red',
    'ERROR': 'darkRed'
}


def log_exceptions(exc_type: Type[BaseException], value: BaseException, tb: TracebackType | None) -> None:
    logging.error(''.join(list(traceback.TracebackException(exc_type, value, tb).format(chain=True))))
    sys.__excepthook__(exc_type, value, tb)


class LoggerSignal(QObject):
    append_logger_signal = Signal(str, str)

    def append_logger(self, color: str, msg: str) -> None:
        self.append_logger_signal.emit(color, msg)


class PySideHandler(logging.Handler):
    def __init__(self) -> None:
        super().__init__()

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        debug = False
        if hasattr(record, 'debug'):
            debug = getattr(record, 'debug')
        if not debug:
            MDGLogger().logger_signal.append_logger(LOGGER_WIDGET_COLORS[record.levelname], msg)


class MDGLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, 'initialized'):
            self.initialized = True
        else:
            return

        if not PathUtils.check_pyinstaller_env():
            FileUtils.remove_folder(PathUtils.LOGS_FOLDER)

        self.logger_signal = LoggerSignal()

        FileUtils.create_folder(PathUtils.LOGS_FOLDER)

        self.log_name = self.get_log_name()
        logging.basicConfig(level=logging.INFO, filename=self.get_path_to_log(),
                            filemode='w',
                            format=LOGGER_FORMAT)

        logger = logging.getLogger()

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(LOGGER_FORMAT))
        logger.addHandler(console_handler)

        pyside_handler = PySideHandler()
        pyside_handler.setFormatter(logging.Formatter(LOGGER_FORMAT))
        logger.addHandler(pyside_handler)

        sys.excepthook = log_exceptions

        logging.info('Logger initialisation complete.')
        logging.debug('Logger initialisation complete.')

    def get_log_name(self) -> str:
        current_date = datetime.now().strftime('%Y-%m-%d')
        current_date_count = 0
        for file in os.listdir(PathUtils.LOGS_FOLDER):
            if file.startswith(current_date):
                current_date_count += 1
        return f'{current_date}-{current_date_count}.log'

    def get_path_to_log(self) -> str:
        return os.path.join(PathUtils.LOGS_FOLDER, self.log_name)
