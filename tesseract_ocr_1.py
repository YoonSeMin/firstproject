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

M = cv2.getRotationMatrix2D((cX, cY), 8, 1.0) #시계반대방향
rot = cv2.warpAffine(image, M, (w, h))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, dst = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#adth = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,2)

cropping = rot[100:500, 50:450] #슬라이싱

den = cv2.fastNlMeansDenoising(gray)

edge = cv2.Canny(image, 100, 200)

contours, hierarchy = cv2.findContours(dst, cv2.RETR_LIST, cv2. CHAIN_APPROX_NONE)


contour = max(contours, key = cv2.contourArea)
contourimg = cv2.drawContours(image, contour, -1, (0,255,0), 4)

cv2.imwrite("result.jpg", contourimg)
#cv2.imshow("result", )


cv2.imwrite("gray.jpg", gray)
cv2.imwrite("binary.jpg", dst)
cv2.imwrite("rotation.jpg", rot)
cv2.imwrite("crop.jpg", cropping)
cv2.imwrite("denoise.jpg", den)
#cv2.imwrite("adaptiveth.jpg", adth)
cv2.imwrite("canny.jpg", edge)




text = image_to_string(contourimg, lang="kor")

with open("sample.txt", "w") as f:
    f.write(text)

