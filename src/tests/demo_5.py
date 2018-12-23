
def fib(times):
    n = 0
    a,b = 0, 1
    while n < times:
        yield b
        a, b = b, a + b
        n += 1
    return "done"



g = fib(2)
next(g)
next(g)
# next(g)