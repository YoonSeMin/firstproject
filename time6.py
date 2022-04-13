# 

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
import time
import threading

from PIL import Image
from pytesseract import *

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

count = 0

def cap():
    global frame
    ret, frame = capture.read()
    job()

def job():
    global count
    cv2.imwrite('D:/OCR/result/threading_timer/frame%d.jpg' % count, frame)
    count += 1
    timer = threading.Timer(3, job)
    timer.start()

cap()

capture.release()
