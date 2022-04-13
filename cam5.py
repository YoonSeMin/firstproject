# 동영상 1초마다 프레임 저장하고 동시에 ocr 글자 추출(종료안됨..)

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

from PIL import Image
from pytesseract import *


filepath = 'D:/OCR/result/prac01.avi'
video = cv2.VideoCapture(filepath)

if not video.isOpened():
    print("Could not Open :", filepath)
    exit(0)

fps = video.get(cv2.CAP_PROP_FPS)
print("fps :", fps)

try:
    if not os.path.exists(filepath[:-4]):
        os.makedirs(filepath[:-4])
except OSError:
    print ('Error: Creating directory. ' +  filepath[:-4])

count = 0

while(video.isOpened()):
    ret, image = video.read()
    if(int(video.get(1)) % fps == 0): #앞서 불러온 fps 값을 사용하여 1초마다 추출
        cv2.imwrite(filepath[:-4] + "/frame%d.jpg" % count, image)
        print('Saved frame number :', str(int(video.get(1))))
        
        text = image_to_string(image, lang="kor")

        with open(filepath[:-4] + "/frame%d.txt" % count, "w") as f:
            f.write(text)
        
        count += 1
        
video.release()

#터미널 종료가 안됨 -> Ctrl + c