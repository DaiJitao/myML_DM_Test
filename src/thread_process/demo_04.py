from multiprocessing import Pool,Manager # 进程池中使用消息队列
import time
import os

p = Pool(3)


qu = Manager().Queue()



p.close()
p.join()
print("end")