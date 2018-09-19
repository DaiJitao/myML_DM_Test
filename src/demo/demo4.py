

def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-2) + fib(n - 1)

def fastFib(n):
    if n == 1 or n == 0:
        return 1
    else:
        _sum = 0
        for i in range(n):
            _sum = _sum + i


if __name__ == "__main__":
    r = fib(3)
    print(r)




