from PIL import Image
import numpy as np
import pickle as pk

jpg = r'E:\pictures\timg.jpg'

pil_im = Image.open(jpg) # 读取图像
# l = pil_im.convert('L')
pil_im.thumbnail((124, 124))

data = np.array(pil_im)
print(data.flatten().size)

print(data.shape, data.size, data.dtype)

data_file = r'E:\pictures\font_pca_modes.pkl'

f = open(data_file, "wb")
pk.dump(data, f)
f.close()




