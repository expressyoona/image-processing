import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/limyoonah.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# a = 5
b = 70
adjusted = cv2.convertScaleAbs(gray, beta=b)

hist = cv2.calcHist([gray],[0],None,[256],[0,256])
adjusted_hist = cv2.calcHist([adjusted],[0],None,[256],[0,256])

plt.subplot(221)
plt.imshow(gray, 'gray')
plt.title('Original')

plt.subplot(222)
plt.imshow(adjusted, 'gray')
plt.title('Adjusted')

plt.subplot(223)
plt.plot(hist)
plt.title('Histogram')

plt.subplot(224)
plt.plot(adjusted_hist)
plt.title('Histogram')


plt.show()
