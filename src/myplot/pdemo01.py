
import matplotlib.pyplot as plt
import numpy as np

dd = np.random.normal(0,1,1000)
y = dd
x = np.arange(1,1001)
plt.plot(y)
plt.grid()
plt.show()

if __name__ == "__main__":
    import pylab
    pylab.figure(1)
    pylab.plot([1,2,3,4], [1,7,3,5])
    pylab.show()
