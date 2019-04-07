import tensorflow as tf
from captcha.image import ImageCaptcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

character = []
# 所有大写字母
for i in range(65, 91):
    character.append(chr(i))
# 所有小写字母
for i in range(97,123):
    character.append(chr(i))
# 所有数字
for i in range(48,58):
    character.append(chr(i))
upper = character[:26]
lower = character[26:52]
number = character[52:]

def random_captcha_text(charset=upper+lower+number, size=4):
    char_text = []
    for i in range(size):
        char_text.append(random.choice(charset))
    return char_text

def get_captcha_text_and_iamge():
    image = ImageCaptcha()
    captcha_text = random_captcha_text()
    captcha_text = "".join(captcha_text)
    captcha = image.generate(captcha_text)
    print(captcha)
    captcha_image = Image.open(captcha)
    print(captcha_image)
    captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image

if __name__ == "__main__":
    text, image = get_captcha_text_and_iamge()
    f = plt.figure()
    ax = f.add_subplot(111)
    ax.text(12, 3, text, ha='center', va='center')
    plt.imshow(image)
    plt.show()

