# cam4+5 : 실시간 웹캠 녹화한 걸로 1초당 프레임 저장해서 OCR 글자 추출

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

from PIL import Image
from pytesseract import *

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:
    ret, frame = capture.read()
    if ret == False:
        break
    
    cv2.imshow("VideoFrame", frame)
    
    key = cv2.waitKey(33)
    
    if key == 27: # Esc
        break
    elif key == 26: # Ctrl + z
        cv2.IMREAD_UNCHANGED
        print("캡쳐")
        cv2.imwrite("D:/OCR/result/" + "rec01" + ".jpg", frame)
    elif key == 24: # Ctrl + x
        print("녹화 시작")
        cv2.IMREAD_UNCHANGED
        record = True
        video = cv2.VideoWriter("D:/OCR/result/" + "rec01" + ".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    elif key == ord('q'):
        print("녹화 중지")
        record = False
        video.release()
        
    if record == True:
        cv2.IMREAD_UNCHANGED
        print("녹화 중..")
        video.write(frame)

capture.release()

cv2.destroyAllWindows()

filepath = 'D:/OCR/result/rec01.avi'
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
