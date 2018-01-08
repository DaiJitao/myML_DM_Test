# _*_ coding:utf-8 _*_
class locker:
    def __init__(self):
        print "locker.__init__() should be not called."

    @staticmethod
    def acquire():
        print("  locker.release() called.（不需要对象实例）")

    @staticmethod
    def release():
        print("  locker.release() called.（不需要对象实例）")

def deco(cls):
    ''' cls '''
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco

@deco(locker)
def myfun():
    print "myfun() called."

myfun()




data = []
path = "/zhaiyao.txt"
with open(path) as file:
    lines = file.readlines()
    for line in lines:
        data.append(line)
