
class A:
    def method(self, arg):
        print("A::", arg)

    def dai_t(self):
        print("dai_t::")

class B(A):
    def method(self, arg):
        #        A.method(self,arg)                # 1
        #        super(B, self).method(arg)    #2
        super().method(arg)  # 3

ob = B()
super(B,ob).method("dai")    #调用class B的父类class A的method。
super(B,ob).dai_t()