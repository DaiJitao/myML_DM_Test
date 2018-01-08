def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco("test")
def myfunc():
    print "myfun() called."

@deco("module2")
def myfunc2():
    print(" myfunc2() called.")

myfunc()
myfunc2()