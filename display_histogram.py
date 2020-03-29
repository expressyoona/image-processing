import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/limyoonah.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([img_gray],[0],None,[256],[0,256])
another_hist = cv2.calcHist([img_gray],[0],None,[128],[0,256])

# Display images
# cv2.imshow('Original', img)
# cv2.imshow('Gray', img_gray)
# cv2.waitKey()

plt.subplot(221)
plt.imshow(img_gray, 'gray')
plt.xticks([]), plt.yticks([])
plt.title('Original')

plt.subplot(222)
plt.plot(hist)
plt.title('Histogram(Max = 256)')

plt.subplot(223)
plt.plot(another_hist)
plt.title('Histogram(Max = 128)')

plt.show()