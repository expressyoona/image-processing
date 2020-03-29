import cv2
from matplotlib import pyplot as plt

def median_filter(original, size):
    if size <= 1 or size % 2 == 0:
        raise Exception('Size must be an odd number and larger than one!')
    # Get width and height of original image
    w, h = original.shape
    r = size//2
    # Extend image r(pixel) every four sides
    result = cv2.copyMakeBorder(original, r, r, r, r, cv2.BORDER_DEFAULT) 
    for x in range(r, w+r):
        for y in range(r, h+r):
            l = []
            for i in range(-r, r+1):
                for j in range(-r, r+1):
                    l.append(result[x+i][y+j])
            l.sort()
            result[x][y] = l[len(l)//2]
    return result

image = cv2.imread('images/noisy_xray.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
median = median_filter(gray, 3)

plt.subplot(131), plt.imshow(image, 'gray'), plt.title('Original')
plt.subplot(132), plt.imshow(median, 'gray'), plt.title('Median')
plt.show()