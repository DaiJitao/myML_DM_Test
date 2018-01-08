
def myfun():
    print "myfun() called"

def deco(fun):
    import pdb
    pdb.set_trace()
    def _deco():
        print "before myfun() called."
        fun()
        print "after myfun() called."
    return _deco

myfun = deco(myfun)
myfun()
myfun()
print "---------------------------------------"

@deco
def myfunc1():
    print "myfunc1() called."

myfunc1()
print "--------------------------------------"