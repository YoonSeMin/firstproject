# 동영상 파일 키 입력받아 녹화 (now는 굳이 필요없을듯)

import cv2
import numpy as np
from matplotlib import pyplot as plt
import datetime

capture = cv2.VideoCapture("test.avi")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("test.avi")

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    key = cv2.waitKey(33)

    if key == 27:
        break
    elif key == 26:
        print("캡쳐")
        cv2.imwrite("D:/OCR/result/" + str(now) + ".jpg", frame)
    elif key == 24:
        print("녹화 시작")
        record = True
        video = cv2.VideoWriter("D:/OCR/result/" + str(now) + ".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    elif key == 3:
        print("녹화 중지")
        record = False
        video.release()
        
    if record == True:
        print("녹화 중..")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()