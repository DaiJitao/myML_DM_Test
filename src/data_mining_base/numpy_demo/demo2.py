import numpy as np

data = np.array([[5, -18], [1,-1]])
print(data)
eigavalue = np.linalg.eig(data)
print(eigavalue)
print(len(eigavalue))
for i in eigavalue:
    print(1)
values = np.linalg.eigvals(data)
print(values)
print("===============")
for i in values:
    print("{:.3f}".format(i))

T = np.array([[2, 1], [0, 3]])
S = np.array([[3, 4], [3, 2]])
print("===========")
print(np.linalg.eigvals(T))
print(np.linalg.eigvals(S))

p = np.array([[3/4, 1/4, 0],
              [1/4, 1/2, 1/4],
              [0, 3/4, 1/4]])
data = p
for i in  range(10):
    data *= p

print("================")
print(data)

for i in  range(10):
    data *= p
print(data)