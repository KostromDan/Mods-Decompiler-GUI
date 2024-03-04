import psutil


def kill_subprocess(proc_pid, kill_child=True):
    try:
        process = psutil.Process(proc_pid)
        if kill_child:
            for proc in process.children(recursive=True):
                proc.kill()
        process.kill()
    except psutil.NoSuchProcess:
        pass
