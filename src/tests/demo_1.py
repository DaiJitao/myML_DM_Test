
def deco(func):
    def _decon(a, b):
        print "before myfun() called."
        ret = func(a, b)
        print "after myfun() called. result: %s" %ret
        return ret
    return _decon

@deco
def myfun(a, b):
    print "myfun(%s, %s) called." %(a, b)
    return a + b

print myfun(1, 2)
print myfun(3, 2)