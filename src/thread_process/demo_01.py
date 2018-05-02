
from multiprocessing import Process
import os
import time
def runproc(test):
    print( test + " my pid id " + str(os.getpid()))
    print(test + " my ppid is " + str(os.getppid()))
    time.sleep(10) # 单位是秒
    # print(test + " is running at id " + os.getpid())

if __name__ == "__main__":
    print("parent process id " + str(os.getpid()))
    p = Process(target = runproc, args = ("daijitao",), name="第一个进程")
    print("sub process is running, my parent_pid is " + str(os.getpid()))
    print(p.name)
    p.start() #
    p.join()  # 告诉父进程，父进程等待子进程执行完毕，父进程再去执行
    print("end")
