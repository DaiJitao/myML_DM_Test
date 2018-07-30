
class Demo():
    def __init__(self):
        self.conn = "12121222"

    def test1(self):
        print("test1")

    def test2(self):
        print("test2")

    def __del__(self):
        print("__del__")

if __name__ == "__main__":
    d = Demo()
    d.test1()
    d.test2()
    m = d
    d.test1()
    d.test2()