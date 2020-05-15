from collections import OrderedDict
import cv2
import numpy as np
from matplotlib import pyplot as plt

def equalization_histogram(img):
    BINS = 255
    x, y = img.shape
    n = x*y
    dic = OrderedDict()
    for i in range(x):
        for j in range(y):
            c = dic.get(img[i][j], 0)
            if c == 0:
                dic[img[i][j]] = 1
            else:
                dic[img[i][j]] += 1

    result = {}
    s = 0
    for level in sorted(dic.keys()):
        count = dic[level]
        s = s + count/n
        result[level] = s

    for i in range(x):
        for j in range(y):
            img[i][j] = int(BINS*result[img[i][j]])
    return img

img = cv2.imread('images/dark.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(121)
plt.imshow(img, 'gray')

after = equalization_histogram(gray)
plt.subplot(122)
plt.imshow(after, 'gray')

plt.show()