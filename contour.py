import pytesseract
import cv2 
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from pytesseract import *

filename = "D:/OCR/picture.png"
image = np.array(Image.open(filename))

(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


contours, hierarchy = cv2.findContours(dst, cv2.RETR_LIST, cv2. CHAIN_APPROX_NONE)
contour = max(contours, key = cv2.contourArea)

contourimg = cv2.drawContours(image, contour, -1, (0,255,0), 4)

cv2.imwrite("result.jpg", contourimg)


cv2.imwrite("gray.jpg", gray)
cv2.imwrite("binary.jpg", dst)


text = image_to_string(gray, lang="kor")

with open("sample.txt", "w") as f:
    f.write(text)

