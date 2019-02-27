import time
import functools

def demo(func):
    @functools.wraps(func)
    def wrapper(n):
        "ok______"
        start = time.time()
        func(n)
        end = time.time()
        runtime = end - start
        print(runtime)
    return wrapper

@demo
def do_this(n):
    "do_this_______"
    for i in range(n):
        pass
    print("game over")


do_this(1000000)


print(do_this.__doc__)

