import cv2
from cv2 import VideoCapture
import numpy as np

cam = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)

while(True):
    ret, frame  = cam.read()
    ranmax = np.array([50,255,50])
    ranmin = np.array([0,51,0])
    mascara = cv2.inRange(frame, ranmin, ranmax)
    opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
    x , y, w, h = cv2.boundingRect(opening)
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 4)
    cv2.circle(frame, (x+w//2, y+h//2), 6, (0,0,100), -1)
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break