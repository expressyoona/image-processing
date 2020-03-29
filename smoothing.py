import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/noisy_xray.jpeg')
# 1 2 3 4 [5] 6 7 8 9
median = cv2.medianBlur(img, 5)
# Size 3x3
aver = cv2.blur(img, (3, 3))

plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(median),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(aver),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()