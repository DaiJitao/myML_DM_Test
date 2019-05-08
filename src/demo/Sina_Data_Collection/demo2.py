import multiprocessing
import time

def writer_proc(q):
    try:
        q.put(1, block = False)
    except:
        pass

def reader_proc(q):
    time.sleep(1)
    try:
        while not q.empty() :
            print(q.get(block = True))
    except:
        pass

if __name__ == "__main__":
    q = multiprocessing.Queue()
    s = []
    for i in range(10):
        writer = multiprocessing.Process(target=writer_proc, args=(q,))
        writer.start()
        s.append(writer)

    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    reader.start()
    # s.append(reader)


    for w in s:
        w.join()
    print("元大小", q.qsize())
    reader.join()
    print("处理后", q.qsize())