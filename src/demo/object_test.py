# _*_ coding:utf-8 _*_

class Animal():
    def __init__(self, canshu):
        self.param = canshu

    def say(self):
        print self.param, "can say"

    def eat(self):
        print self.param, "can eat"

    def run(self):
        print self.param, "can run"


dog = Animal("5")
dog.say()

cat = Animal("cat")
cat.run()


def say():
    print 'can say'


say()


def run(R):
    print R, 'can run'


run('m')


def say1(s1, s2):
    print s1, 'can say '
    print s2, 'can say too'


say1('m1', 'm1')


def say2(*si):
    print len(si)


say2("m", "my")

i = 0
while i <= 100000:
    i = i + 1
    if i == 100:
        continue
        print i
b = []
i = 0
while i <= 4:
    i = i + 1
    b.append(i)
print b

data = [j for j in range(1,101) if j%2==0 and j%3!=0]
print data



