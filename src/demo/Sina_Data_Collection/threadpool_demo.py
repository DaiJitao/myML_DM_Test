from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing

cpu_num = multiprocessing.cpu_count()

pool = ThreadPool(cpu_num)
