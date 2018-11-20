from PIL import Image
from time import sleep
from pylab import *

path = r'E:\pictures\timg.jpg'

im = array(Image.open(path))
imshow(im)


print('3 clicks')
x = ginput(3)
sleep(55)
print(":::==>", x)
show()