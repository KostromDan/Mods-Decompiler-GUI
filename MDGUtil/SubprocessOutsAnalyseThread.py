import logging
import multiprocessing
import subprocess
import sys
import threading
from collections import OrderedDict
from typing import Callable, TextIO, Any


class SubprocessOutAnalyseThread(threading.Thread):
    def __init__(self,
                 cmd: subprocess.Popen,
                 line_count: multiprocessing.Value,
                 cmd_out: subprocess.PIPE,
                 sys_out: TextIO,
                 logger: Callable[[str], Any],
                 repeat_output_to_sys_out: bool) -> None:
        super().__init__()
        self.cmd = cmd
        self.line_count = line_count
        self.cmd_out = cmd_out
        self.sys_out = sys_out
        self.logger = logger
        self.repeat_output_to_sys_out = repeat_output_to_sys_out
        self.out_lines: dict[int, str] = dict()
        self.current_line: list[str] = []

    def run(self) -> None:
        while True:
            symbol = self.cmd_out.read(1).decode(errors='ignore')
            if symbol == '' and self.cmd.poll() is not None:
                break
            if symbol != '':
                if self.repeat_output_to_sys_out:
                    self.sys_out.write(symbol)
                    self.sys_out.flush()
                self.current_line.append(symbol)
                if symbol == '\n':
                    line = ''.join(self.current_line).rstrip('\n\r')
                    if line != '':
                        with self.line_count.get_lock():
                            self.out_lines[self.line_count.value] = line
                            self.line_count.value += 1
                        self.logger(line)
                    self.current_line.clear()


class SubprocessOutsAnalyseThread(threading.Thread):
    def __init__(self,
                 cmd: subprocess.Popen,
                 stdout: TextIO = sys.stdout,
                 stderr: TextIO = sys.stderr,
                 std_logger: Callable[[str], Any] = logging.info,
                 err_logger: Callable[[str], Any] = logging.error,
                 repeat_output_to_sys_out: bool = False) -> None:
        super().__init__()
        self.cmd = cmd
        self.out = None
        self.err = None
        self.all = None
        self.stdout = stdout
        self.stderr = stderr
        self.std_logger = std_logger
        self.err_logger = err_logger
        self.repeat_output_to_sys_out = repeat_output_to_sys_out

    def run(self) -> None:
        line_count = multiprocessing.Value('i', 0)
        stdout_thread = SubprocessOutAnalyseThread(self.cmd, line_count,
                                                   self.cmd.stdout, self.stdout,
                                                   self.std_logger, self.repeat_output_to_sys_out)
        stderr_thread = SubprocessOutAnalyseThread(self.cmd, line_count,
                                                   self.cmd.stderr, self.stderr,
                                                   self.err_logger, self.repeat_output_to_sys_out)
        stdout_thread.start()
        stderr_thread.start()
        stdout_thread.join()
        stderr_thread.join()
        self.out = '\n'.join(OrderedDict(sorted(stdout_thread.out_lines.items(), key=lambda x: x[0])).values())
        self.err = '\n'.join(OrderedDict(sorted(stderr_thread.out_lines.items(), key=lambda x: x[0])).values())
        all_dict = dict()
        all_dict.update(stderr_thread.out_lines)
        all_dict.update(stdout_thread.out_lines)
        self.all = '\n'.join(OrderedDict(sorted(all_dict.items(), key=lambda x: x[0])).values())
        print(self.out)
        print(self.err)
        print(self.all)
