c = 12
def Demo():
    global c
    c = 22
    return c


m = Demo()

print("c =", c)
print("test =", Demo())


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
f = fib(1)
print(next(f))
f.__next__()

def fun():
    a = 10
    b = 20
    print(locals())

def gen(x):
    n = 0
    while n < x:
        t = yield n * 2
        print(t)
        n += 1
    return 'done'



def line_conf(a, b):
    def line(x):
        return a * x + b
    return line

class School():
    def __init__(self, s1):
        self.subject1 = s1
        self.subject2 = "cpp"

    def __getattribute__(self, item):
        if item == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            return object.__getattribute__(self, item)



print("===================")
s= School("python")
print(s.subject1)
print(s.subject2)


def out(a, b):
    def inner(x):
        return a * x + b
    return inner