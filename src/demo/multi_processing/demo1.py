import os
import multiprocessing

pid = os.fork()

if pid < 0:
    print("fork() error")
elif pid == 0:
    print("PPid: (%s), pid:(%s)" %(os.getppgid(), os.getpgid()))