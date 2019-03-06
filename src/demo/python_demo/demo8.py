<<<<<<< HEAD
import functools

def show(*args, **kwargs):
    print(args)
    print(kwargs)

p1 = functools.partial(show, 1,2,3)
p1()
p1(4,5,6)
p1(name='dai')
print("===========================================")
def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print("note something")
        return func()
    return wrapper

@note
def demo():
    """test demo"""
    print("I am demo")




class Person():
    def __getattribute__(self, item):
        print("getattribute")
        if item.startwith("a"):
            print("hhhhhhhhhhhaaaaaaaaaaaaa")
        else:
            return self.test

    def test(self):
        print("test")


class School(object):
    def __init__(self, sub1):
        self.sub1 = sub1
        self.sub2 = 'cpp'

    def __getattribute__(self, item):
        if item == 'sub1':
            print("dai log")
            return "dai log"
        elif item == 'sub2':
            print("cpp log")
            return "cpp log"
        else:
            return object.__getattribute__(self, item)

    def test(self):
        print("test")

print("===========================================")
s = School("dai")
# print(s.sub1)
s.a = 12
print(s.test())
=======
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

>>>>>>> 5f0e407a502a793a8e4d948a420ff81e86c46e34
