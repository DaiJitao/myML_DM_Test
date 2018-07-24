import seaborn as sns
iris = sns.load_dataset('iris')
print(type(iris))
dh = iris.head()
print(dh)

sns.set()
dd = sns.pairplot(iris, hue='species', size=5)


class A():

    d = 12
    a = 11

    def test(self):
        print(d)

a = A()
a.test()
