c = 12


def Demo():
    global c
    c = 22
    return c


m = Demo()

print("c=", c)
print("test=", Demo())


#
def fib(times):
    a, b = 0, 1
    n = 0
    if times == 0: return n
    while n < times:
        c = yield b
        print(c)
        a, b = b, a + b
        n += 1
    return "ok done!"

def fun():
    a = 10
    b = 20
    print(locals())


if __name__ == "__main__":
    fun()
