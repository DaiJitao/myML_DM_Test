
def deco(func):
    def _deco(*args, **kwargs):
        print "before %s called." % func.__name__
        ret = func(*args, **kwargs)
        print "after %s called. result: %s" % (func.__name__, ret)
        return ret
    return _deco

@deco
def myfun(a, b):
    print "myfun(%s, %s) called." %(a, b)
    return a + b

@deco
def myfun2(a, b, c):
    print "myfun(%s, %s, %s) called." %(a, b, c)
    return a + b + c

myfun(12,12)
