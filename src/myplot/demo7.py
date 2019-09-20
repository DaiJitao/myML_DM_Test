import numpy as np
import matplotlib.pyplot as plt

# 在我的 notebook 里，要设置下面两行才能显示中文
plt.rcParams['font.family'] = ['sans-serif']
# 如果是在 PyCharm 里，只要下面一行，上面的一行可以删除
plt.rcParams['font.sans-serif'] = ['SimHei']

x = ["2018-9", "2018-10", "2018-11", "2018-12", "2019-1", "2019-2", "2019-3", "2019-4", "2019-5", "2019-6", "2019-7",
     "2019-8", "2019-9"]
xiongan = [447, 1869, 986, 1805, 7259, 3638, 1378, 3221, 2298, 1765, 2510, 2074, 979]
sh = [1095, 3693, 6910, 4630, 6762, 9613, 7980, 6888, 6037, 3843, 5768, 11644, 3236]

plt.plot(x, xiongan)
plt.plot(x, sh)
plt.xlabel("p(x)")
plt.ylabel("H(x)")
# plt.grid(True)
plt.show()
