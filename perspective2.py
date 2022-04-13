import cv2
import numpy as np
from matplotlib import pyplot as plt

import pytesseract
from PIL import Image
from pytesseract import *

img_source = cv2.imread('D:/OCR/cam8.jpg')
img_gray = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY)
img_denoise = cv2.fastNlMeansDenoising(img_gray, None, 9, 3, 5)
img_adaptive = cv2.adaptiveThreshold(img_denoise, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 4)

kernel_1 = cv2.getStructuringElement(cv2.MORPH_CROSS, (50, 50))
kernel_2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (10, 10))

img_close = cv2.morphologyEx(img_adaptive, cv2.MORPH_OPEN, kernel_1)
img_open = cv2.morphologyEx(img_close, cv2.MORPH_CLOSE, kernel_1)

img_canny = cv2.Canny(img_open, 125, 200)

contours, hierachy= cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_outline = cv2.drawContours(img_source, contours, -1, (0,255,0), 1)



pts1 = np.float32([[417,89],[408,592],[971,92],[942,652]])
pts2 = np.float32([[10,10],[10,1000],[1000,10],[1000,1000]])

#cv2.circle(img_source, (417,89), 20, (255,0,0),-1)
#cv2.circle(img_source, (408,592), 20, (0,255,0),-1)
#cv2.circle(img_source, (971,92), 20, (0,0,255),-1)
#cv2.circle(img_source, (942,652), 20, (0,0,0),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img_adaptive, M, (1100,1100)) #img_source


plt.subplot(121),plt.imshow(img_source),plt.title('image') #img_source
plt.subplot(122),plt.imshow(dst),plt.title('Perspective') #dst
plt.show()

text = image_to_string(dst, lang="kor")

with open("sample.txt", "w") as f:
    f.write(text)