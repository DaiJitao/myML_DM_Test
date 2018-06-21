import time
import sys
from functools import reduce

def test():
    n = 0
    while True:
        for i in range(1000):
            n += 1
        time.sleep(1)
        if n == 1000:
            break
    print("=====>ok")

if __name__=="__main__":
    # test()
    # i = sys.exit(test())
    # print(i)
    # print(sys.platform())
    data = map(lambda x : x * 2, [1, 2, 3])
    print("data ", data)




