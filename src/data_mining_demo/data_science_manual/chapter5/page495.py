import seaborn as sns
iris = sns.load_dataset('iris')
print(type(iris))
dh = iris.head()
print(dh)

sns.set()
dd = sns.pairplot(iris, hue='species', size=5)

import matplotlib.pylab as plt
import numpy as np
