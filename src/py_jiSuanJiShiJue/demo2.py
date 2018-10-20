

import pickle as pk

data_file = r'E:\pictures\font_pca_modes.pkl'
f1 = open(data_file, "rb")
dd = pk.load(f1)
print(dd)
f1.close()