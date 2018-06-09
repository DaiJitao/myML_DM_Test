import threading
import time

g_num = 0
def worker():
    global g_num, mutex_lock # 每个线程都获得这个全局变量
    for i in range(100000):
        mutex_lock.acquire()
        g_num += 1
        mutex_lock.release()
# if __name__ == "__main__":
    # 创建互斥锁
mutex_lock = threading.Lock()
t1 = threading.Thread(target=worker)
t1.start()
t2 = threading.Thread(target=worker)
t2.start()
print("g_num:%d" % g_num)
