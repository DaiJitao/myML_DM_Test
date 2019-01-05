
class Demo():
    def __call__(self, *args, **kwargs):
        print("call me")

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

a = 12
if __name__ == "__main__":
    def print_dd():
        global a
        a = 15

    d = Demo()
    d()






