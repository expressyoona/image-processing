import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/SanFrancisco.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray, (3,3), 0)

# Canny
img_canny = cv2.Canny(img, 100, 200)

# Sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely

# Prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

# Laplacian
img_laplacian = cv2.Laplacian(img_gaussian, cv2.CV_64F)

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('Original')
plt.subplot(232), plt.imshow(img_canny, 'gray'), plt.title('Canny')
plt.subplot(233), plt.imshow(img_sobel, 'gray'), plt.title('Sobel')
plt.subplot(234), plt.imshow(img_prewittx + img_prewitty, 'gray'), plt.title('Prewitt')
plt.subplot(235), plt.imshow(img_laplacian, 'gray'), plt.title('Laplacian')
plt.show()