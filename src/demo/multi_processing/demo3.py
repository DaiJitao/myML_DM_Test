import threading


class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)  # 初始化线程

    def run(self):
        for i in range(10):
            print("我是线程A")


class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)  # 初始化线程

    def run(self):
        for i in range(10):
            print("我是线程B")


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        pass


if __name__ == "__main__":
    t1 = A()
    t1.start()
    t2 = B()
    t2.start()
