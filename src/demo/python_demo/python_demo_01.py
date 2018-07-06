

def decorated_by(func):
    func.__doc__ = str(func.__doc__) + "\n Decorated by decorated_by."
    return func

@decorated_by
def add(x, y):
    return x + y

registry = []
def register(decorated):
    registry.append(decorated)
    return decorated


# foo()
# bar()
# answer = []
# for func in registry:
#     answer.append(func())
class Register(object):
    def __init__(self):
        """ """
        self._functions = []
        print("init: ", self._functions)

    def register(self, func):
        self._functions.append(func)
        print("register: ", self._functions)
        return func

    def run_all(self, *args, **kwargs):
        return_values = []
        print(self._functions)
        for func in self._functions:
            print("func ", func)
            return_values.append(func(*args, **kwargs))
        return return_values

a = Register()
b = Register()

@a.register
def foo(x = 3):
    return x

@b.register
def bar(x = 5):
    return x

@a.register
@b.register
def baz(x = 7):
    return x



import functools

# def requir_ints(decorated):
#     @functools.wraps(decorated)
#     def inner(*args, **kwargs):
#         kwargs_values = [i for i in kwargs.values()]
#         for arg in args + kwargs_values:
#             if not isinstance(i, int):
#                 raise TypeError("error!")


class User(object):
    def __init__(self, username, email):
        self.username = username
        self.email = email

class AnonymousUser(User):
    def __init__(self):
        self.username = None
        self.email = None

    def __nonzero__(self):
        return False


import json

def json_output(decorated):
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        """ test """
        result = decorated(*args, **kwargs)
        return json.dump(result)
    return inner

@json_output
def do_nothing():
    """ dddd"""
    return {"name": "daijitao"}

help(json_output)











