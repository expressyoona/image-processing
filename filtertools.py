import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
filter_from_kernel: filter image with a specific kernel
original: Source
kernel: Matrix size 3x3
"""
def filter_from_kernel(original, kernel):
    r = 1
    image = cv2.copyMakeBorder(original, r, r, r, r, cv2.BORDER_DEFAULT)
    w, h = original.shape
    for x in range(1, w-1):
        for y in range(1, h-1):
            image[x][y] = (kernel[0][0]*original[x-1][y+1] + kernel[0][1]*original[x][y+1] + kernel[0][2]*original[x+1][y+1]
                            + kernel[1][0]*original[x-1][y] + kernel[1][1]*original[x][y] + kernel[1][2]*original[x+1][y]
                            + kernel[2][0]*original[x-1][y-1] + kernel[2][1]*original[x][y-1] + kernel[2][2]*original[x+1][y-1])
    return image


img = cv2.imread('images/grid.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplacian_kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
# laplacian_kernel = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
# laplacian_kernel = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
laplacian = filter_from_kernel(gray, laplacian_kernel)
laplacian = -laplacian

plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(laplacian, 'gray'), plt.title('Laplacian')
plt.xticks([]), plt.yticks([])
plt.show()