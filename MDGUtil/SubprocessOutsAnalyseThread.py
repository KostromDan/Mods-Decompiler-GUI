import logging
import sys
import threading


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
            symbol = self.cmd_out.read(1).decode()
            if symbol == '' and self.cmd.poll() is not None:
                break
            if symbol != '':
                # self.sys_out.write(symbol)
                # self.sys_out.flush()
                self.current_line.append(symbol)
                if symbol == '\n':
                    line = ''.join(self.current_line).rstrip('\n').rstrip('\r')
                    if line != '':
                        self.out_lines.append(line)
                        self.logger(line)
                    self.current_line.clear()


class SubprocessOutsAnalyseThread(threading.Thread):
    def __init__(self, cmd):
        super().__init__()
        self.cmd = cmd
        self.out = None
        self.err = None

    def run(self):
        stdout_thread = SubprocessOutAnalyseThread(self.cmd, self.cmd.stdout, sys.stdout, logging.info)
        stderr_thread = SubprocessOutAnalyseThread(self.cmd, self.cmd.stderr, sys.stderr, logging.error)
        stdout_thread.start()
        stderr_thread.start()
        stdout_thread.join()
        stderr_thread.join()
        self.out = '\n'.join(stdout_thread.out_lines)
        self.err = '\n'.join(stderr_thread.out_lines)
