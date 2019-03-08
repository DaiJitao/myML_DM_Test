import pandas as pd

data_file = "./unrate.csv"

unrate = pd.read_csv(data_file)
unrate['DATE'] = pd.to_datetime(unrate['DATE'])


import matplotlib.pyplot as plt

plt.plot(unrate['DATE'], unrate["VALUE"])
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

fig = plt.figure(figsize=(30, 3))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

plt.show()

unrate['MONTH'] = unrate['DATE'].dt.month
print(unrate.head())
plt.figure(figsize=(10, 3))
colors = ['blue', 'green', 'red', 'yellow', 'black']
for i in range(5):
    start_index = i * 12
    end_index = (i+1) * 12
    subset = unrate[start_index:end_index]

    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c = colors[i], label = label)
plt.legend(loc = 'best')
plt.show()



