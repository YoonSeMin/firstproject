import cv2
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

from PIL import Image
from pytesseract import *

img_source = cv2.imread('D:/OCR/result/cap01.jpg')
img_gray = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY)
img_denoise = cv2.fastNlMeansDenoising(img_gray, None, 9, 3, 5)
#ret, dst = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
img_adaptive = cv2.adaptiveThreshold(img_denoise, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 4)

kernel_1 = cv2.getStructuringElement(cv2.MORPH_CROSS, (50, 50))
kernel_2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (10, 10))

img_close = cv2.morphologyEx(img_adaptive, cv2.MORPH_OPEN, kernel_1)
img_open = cv2.morphologyEx(img_close, cv2.MORPH_CLOSE, kernel_1)

img_canny = cv2.Canny(img_open, 125, 200)

contours, hierachy= cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#contour = max(contours, key = cv2.contourArea)
img_outline = cv2.drawContours(img_source, contours, -1, (0,255,0), 1)

images = [img_gray, img_adaptive, img_close, img_open, img_canny, img_outline]
titles = ['Gray', 'Adaptive_Threshold', 'Close', 'Open', 'Canny_Edge', 'Contours']

for i in range(6):
    plt.subplot(2, 3, i+1),plt.imshow(images[i], cmap='gray', aspect='auto'),plt.title(titles[i]),plt.tight_layout()
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.imshow('img', img_adaptive)

cv2.waitKey()

cv2.destroyAllWindows()


text = image_to_string(img_adaptive, lang="kor")

with open("sample.txt", "w") as f:
    f.write(text)