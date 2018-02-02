
def decorated_by(func):
    func.__doc__ += "\nDecorated by decorated_by\n"
    return func

def add(x, y):
    """return the sum """
    return x + y

add = decorated_by(add)
print(add(12,12))

registry = []
def register(decorated):
    registry.append(decorated)
    return decorated

@register
def foo():
    return 3
@register
def bar():
    return 5

answerd = []
for func in registry:
    answerd.append(func())

for i in answerd:
    print(i)


