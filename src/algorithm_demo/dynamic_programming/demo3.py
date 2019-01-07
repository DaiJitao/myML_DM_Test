import time


def solution(n):
    if n == 0:
        return 1
    else:
        return n * solution(n - 1)


def get_time(func):
    def wratter(count):
        start = time.time()
        func(count)
        runtime = time.time() - start
        print(func.__name__, "time: ", str(runtime))

    return wratter


def fib(n):
    if n < 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def fib2(n):
    result = [0] * n
    if n == 2: return 2
    if n == 1: return 1
    if n < 0:
        return 0
    else:
        result[0] = 0
        result[1] = 1
        result[2] = 1


start = time.time()
print(fib(33))
print((time.time() - start) * 60)
