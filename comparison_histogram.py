import cv2
from matplotlib import pyplot as plt
# from matplotlib import image

first_img = cv2.imread('images/grid_hor_ver.png')
second_img = cv2.imread('images/grid_horizontal.png')
third_img = cv2.imread('images/grid_vertical.png')

first_img_gray = cv2.cvtColor(first_img, cv2.COLOR_BGR2GRAY)
second_img_gray = cv2.cvtColor(second_img, cv2.COLOR_BGR2GRAY)
third_img_gray = cv2.cvtColor(third_img, cv2.COLOR_BGR2GRAY)

first_hist = cv2.calcHist([first_img_gray],[0],None,[256],[0,256])
second_hist = cv2.calcHist([second_img_gray],[0],None,[256],[0,256])
third_hist = cv2.calcHist([third_img_gray],[0],None,[256],[0,256])


# Display histograms
plt.subplot(3, 2, 1)
plt.imshow(first_img, 'gray')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 2)
plt.plot(first_hist)
plt.title('First histogram')

plt.subplot(3, 2, 3)
plt.imshow(second_img, 'gray')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 4)
plt.plot(second_hist)
plt.title('Second histogram')


plt.subplot(3, 2, 5)
plt.imshow(third_img, 'gray')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 6)
plt.plot(third_hist)
plt.title('Third histogram')

plt.show()