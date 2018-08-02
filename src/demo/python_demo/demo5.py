


class DistanceForm(object):
    def __init__(self, o):
        self.o = o
        print("init::%s", o)

    def __call__(self, x):
        print("X::%s", x)

p = DistanceForm(12)
p('2000')


def decorated_by(func):
    func.__doc__ = "jjjjjjjjjjj"
    func.__repr__ = "add"
    func.name = 12

    return func

@decorated_by
def add_(a, b):
    return 1 + b

myAdd = add_
print(myAdd(12,12))
print(myAdd.__doc__)
print("d::", myAdd.name)



##===========================================

regi = []
def register(decorated):
    regi.append(decorated)
    return decorated

@decorated_by # 最后执行
@register # 最先执行
def foo():
    return 23


@decorated_by
@register
def bar():
    return 23

for i in regi:
    print(i)
    print(i.name)











