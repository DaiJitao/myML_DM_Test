import threading
import time


def saySorry(test):
    print("我错了" + test)
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry, args=("daijitao",))
        t.start()
