import threading
import time


def express1(n):
    print('this is', n)
    time.sleep(2)


def express2(m, l):
    print('this is', m, l)
    time.sleep(2)


s1 = threading.Thread(target=express1, args=('one', ))
s2 = threading.Thread(target=express2, args=('two', 'test'))
s1.start()
s2.start()
