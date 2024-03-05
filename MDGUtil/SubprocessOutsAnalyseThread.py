import logging
import sys
import threading
import time

from MDGUtil.SubprocessKiller import kill_subprocess


class SubprocessOutAnalyseThread(threading.Thread):
    def __init__(self, cmd, cmd_out, sys_out, logger):
        super().__init__()
        self.cmd = cmd
        self.cmd_out = cmd_out
        self.out_lines = []
        self.current_line = []
        self.sys_out = sys_out
        self.logger = logger

    def run(self):
        while True:
            symbol = self.cmd_out.read(1).decode(errors='ignore')
            if symbol == '' and self.cmd.poll() is not None:
                break
            if symbol != '':
                # self.sys_out.write(symbol)
                # self.sys_out.flush()
                self.current_line.append(symbol)
                if symbol == '\n':
                    line = ''.join(self.current_line).rstrip('\n\r')
                    if line != '':
                        self.out_lines.append(line)
                        self.logger(line)
                    self.current_line.clear()


class SubprocessOutsAnalyseThread(threading.Thread):
    def __init__(self, cmd, stdout=sys.stdout, stderr=sys.stderr, std_logger=logging.info, err_logger=logging.error,
                 timeout=None, on_timeout_kill_child=True):
        super().__init__()
        self.cmd = cmd
        self.out = None
        self.err = None
        self.stdout = stdout
        self.stderr = stderr
        self.std_logger = std_logger
        self.err_logger = err_logger
        self.timeout = timeout
        self.on_timeout_kill_child = on_timeout_kill_child

    def run(self):
        stdout_thread = SubprocessOutAnalyseThread(self.cmd, self.cmd.stdout, self.stdout, self.std_logger)
        stderr_thread = SubprocessOutAnalyseThread(self.cmd, self.cmd.stderr, self.stderr, self.err_logger)
        stdout_thread.start()
        stderr_thread.start()
        if self.timeout is not None:
            time.sleep(self.timeout)
            if stdout_thread.is_alive() or stderr_thread.is_alive():
                kill_subprocess(self.cmd.pid, kill_child=self.on_timeout_kill_child)
        stdout_thread.join()
        stderr_thread.join()
        self.out = '\n'.join(stdout_thread.out_lines)
        self.err = '\n'.join(stderr_thread.out_lines)
