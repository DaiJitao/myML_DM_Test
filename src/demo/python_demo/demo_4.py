class X(object):
    def __init__(self, a, b, range):
        self.a = a
        self.b = b
        self.range = range
    def __call__(self, a, b):
        self.a = a
        self.b = b
        print('__call__ with （{}, {}）'.format(self.a, self.b))
    def __del__(self, a, b, range):
        del self.a
        del self.b
        del self.range


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    def go_to_vet(self):
        pass

class Cat(Animal):
    def menow(self):
        pass
    def purr(self):
        pass


###############################################
def init(self, name):
    self.name = name

def eat(self):
    pass

def go_to_vet(self):
    pass

Animal_2 = type("Animal_2", (object,), {'__doc__':"hhhhhhhh",
                                        "__init__":init,
                                        'eat':eat,
                                        'go_to_vet':go_to_vet})

a = Animal_2("cat")
print(a.name)
print(a.__doc__)

