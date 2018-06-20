a= "a"

def print_demo(data):
    print("data ", data)
print_demo("/root/sd%s" %a )


class MyClass(object):
    def __del__(self):
        print("AAAAAAAAAAAAAAAA")


class TimeSpan(object):
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours;
        self.minutes= minutes;
        self.seconds= seconds

    def __repr__(self):
        return "hours=%d, minutes=%d" %(self.hours, self.minutes)


import abc


class AbstractDict(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def foo(self):
        return None


class MyTest(AbstractDict):
    def __init__(self):
        pass

a = TimeSpan()

print("a", a)
