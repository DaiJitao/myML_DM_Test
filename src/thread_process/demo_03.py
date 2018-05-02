from multiprocessing import Process
import os
import time

class myProcess(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print("sub process")
        start = time.time()
        time.sleep(self.interval)
        end = time.time()
        print("进程ID=" + str(os.getpid())+ " 父进程="+ str(os.getppid()) + " 时间差=" + str(end-start))


if __name__ == "__main__":
    print("main process...")
    start = time.time()
    p = myProcess(2)
    p.start()
    p.join()
    end = time.time()
    print("main process time " + str(end - start))