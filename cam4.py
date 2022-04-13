# webcam 키 입력받아 녹화 동영상 저장

import cv2
import numpy as np
from matplotlib import pyplot as plt

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
        cv2.IMREAD_UNCHANGED
        print("녹화 시작")
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