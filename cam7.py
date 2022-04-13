# schedule module 사용 >> 설치 오류, 해결 못함...ㅠ

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
import time
import schedule

from PIL import Image
from pytesseract import *

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
count = 0
filepath = 'D:/OCR/result/'

def job():
    cv2.imwrite(filepath[:-4] + "/frame%d.jpg" % count, frame)
    count += 1

while True:
    ret, frame = capture.read()
    if ret == False:
        break
    
    cv2.imshow("VideoFrame", frame)
    
    key = cv2.waitKey(33)
    
    if key == 27: # Esc
        break
    
    else :
        cv2.IMREAD_UNCHANGED
        schedule.every(3).seconds.do(job)
        

capture.release()

cv2.destroyAllWindows()
