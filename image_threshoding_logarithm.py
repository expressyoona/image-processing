import cv2
from math import log10
from matplotlib import pyplot as plt

def thresholding(image, threshold):
    row, column = image.shape
    for i in range(row):
        for j in range(column):
            if image[i][j] > threshold:
                image[i][j] = 255
            else:
                image[i][j] = 0
    return image

def logarithmic_transformation(image, c=1):
    row, column = image.shape
    for i in range(row):
        for j in range(column):
            image[i][j] = c*log10(image[i][j] + 1)
    return image


first = cv2.imread('images/gradient.jpg')
first_gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
first_result = thresholding(first_gray, 127)

second = cv2.imread('images/einstein.jpg')
second_gray = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)
second_result = logarithmic_transformation(second_gray)

plt.subplot(2, 2, 1)
plt.imshow(first, 'gray')
plt.xticks([]), plt.yticks([])
plt.title('1st image')

plt.subplot(2, 2, 2)
plt.imshow(first_result, 'gray')
plt.xticks([]), plt.yticks([])
plt.title('After thresholding')

plt.subplot(2, 2, 3)
plt.imshow(second, 'gray')
plt.xticks([]), plt.yticks([])
plt.title('2nd image')

plt.subplot(2, 2, 4)
plt.imshow(second_result, 'gray')
plt.xticks([]), plt.yticks([])
plt.title('After logarithmic transformation')

plt.show()