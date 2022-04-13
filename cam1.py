# webcam 연결, 이미지 캡처

import cv2
import numpy as np
from matplotlib import pyplot as plt

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test.avi',fourcc, 20.0, (640,480))

while True:
    ret, frame = capture.read()
    if ret == False:
        break
    
    out.write(frame)
    
    cv2.imshow("VideoFrame", frame)
    
    img = np.zeros(frame.shape, np.uint8)
    
    key = cv2.waitKey(1)
    if key ==27:
        break
    elif key == 26: # Ctrl + z
        cv2.IMREAD_UNCHANGED #원본 사용
        cv2.imwrite("D:/OCR/result/cap01" + ".jpg", frame)

capture.release()

cv2.destroyAllWindows()