import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_kek = cv.imread('Zhumazhenis.jpg', 1) #uploading an image
img_kek = img_kek[30:213, 30:278]
img_kek = cv.cvtColor(img_kek,cv.COLOR_BGR2RGB) #converting to RGB as MATLAB recognizes only RGB

img_kek_hsv=cv.cvtColor(img_kek, cv.COLOR_RGB2HSV) #converting to HSV

lower_red = np.array([0,0,244]) #setting boundaries of red colour
upper_red = np.array([255,255,255])
mask = cv.inRange(img_kek_hsv, lower_red, upper_red) #creating mask

img_kek_result = cv.bitwise_and(img_kek, img_kek, mask=mask) #bitwise AND Operation

titles = ['Original image', 'BGR to HSV', 'Mask', 'Hottest Segments'] #plotting the results
images = [img_kek, img_kek_hsv, mask, img_kek_result]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()