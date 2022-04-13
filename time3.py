# 3초마다 프레임 저장, 하지만 잘 안됨ㅋ

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
import time
import threading

from PIL import Image
from pytesseract import *

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

count = 0
#fps = int(capture.get(cv2.CAP_PROP_FPS))
#print(fps)
fps = capture.set(cv2.CAP_PROP_FPS, 20)


def job():
    global count
    if(int(capture.get(1)) % fps == 0):
        cv2.imwrite('D:/OCR/result/threading_timer/frame%d.jpg' % count, frame)
        count += 1
    timer = threading.Timer(3, job)
    timer.start()

while True:
    ret, frame = capture.read()
    if ret == False:
        break
    
    cv2.imshow("VideoFrame", frame)
    
    key = cv2.waitKey(33)
    
    if key == 27: # Esc
        break
    
    else :
        if(int(capture.get(1)) % (fps*3) == 0):
            cv2.IMREAD_UNCHANGED
            job()
        

capture.release()

cv2.destroyAllWindows()