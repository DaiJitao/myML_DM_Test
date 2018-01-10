#coding=utf-8

def say_goodbye():
    print("hello")

# if __name__ == '__main__':
#     say_hello()
#     say_goodbye()

def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

def debug_2(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        print("args ", args)
        print("kwargs ", kwargs)
        return func(*args, **kwargs)
    return wrapper

def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[[level]] enter function {func}()".format(level=level, func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level="01")
def say_hello(p):
    print("hello {}".format(p))

class Test():
    def __call__(self, *args, **kwargs):
        print("call me")

t = Test()
t()