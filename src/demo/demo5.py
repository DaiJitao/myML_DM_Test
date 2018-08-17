
a = 12
def fun():
    a = 123

fun()
print(a)


class A(object):
    def foo(self, x):
        print ("foo::executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo::(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo::(%s)" % x)

a = A()
a.class_foo(12)
a.static_foo(12)
a.foo(12)
A.static_foo(121)
A.class_foo(121)

def print_everything(*args):
    for c , th in enumerate(args):
        print('{0} {1}'.format(c, th))

print_everything('qq','qqqq')
