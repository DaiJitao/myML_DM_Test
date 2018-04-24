# _*_ coding:utf-8 _*_
class Car:
    def __init__(self):
        self.name = 12
        self.age = 22
        self.color = "red"

    def start(self):
        """
        """
        print("ok")

    def __str__(self):
        return "djt"

class myCar(Car):
    def __init__(self):
        print("==============")

    @classmethod
    def test(cls):
        print("test")

    @staticmethod
    def test3():
        print("static")



car = Car() # 在内存中占用一定的空间

car.start()
car.__name = 123
print(car)
myCar().test()


"""
"""
class People(object):
    name = "人类" #类属性 共有
    __pwd = "123"

    @classmethod
    def test(cls):
        print(type(cls))
        print(cls)

    @staticmethod #静态方法
    def test3():
        People.name = "hahha"
        print(People.name)


pp = People()
People.test()
print(pp.name)