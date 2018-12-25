def doca(func):
    def wrapper():
        print(func.__name__)
        func()

    return wrapper


def fun():
    print("---1---")


@doca
def fun2():
    print("===2===")


fun2()
