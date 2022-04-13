# 동영상 파일 키 입력받아 녹화, 1초마다 프레임 추출(이건 실패)

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
    elif key == 26:
        cv2.IMREAD_UNCHANGED #원본 사용
        cv2.imwrite("D:/OCR/result/cap01" + ".jpg", frame)

capture.release()

cv2.destroyAllWindows()

#////////////////////////////////////////////////////////////////////

video = cv2.VideoCapture('test.avi')
fps = video.get(cv2.CAP_PROP_FPS)

count = 0

while(video.isOpened()):
    ret, image = video.read()
    if(int(video.get(1)) % fps == 0): #앞서 불러온 fps 값을 사용하여 1초마다 추출
        cv2.imwrite('D:/OCR/result'[:-4] + "/frame%d.jpg" % count, image)
        print('Saved frame number :', str(int(video.get(1))))
        count += 1
        
video.release()
