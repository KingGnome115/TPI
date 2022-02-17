import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    
    colorO = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    cv2.imshow('Frame Color',colorO)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame Gray',gray)

    HLS = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    cv2.imshow('Frame HLS',HLS)

    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('Frame HSV',HSV)

    YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    cv2.imshow('Frame YUV',YUV)

    CrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    cv2.imshow('Frame CrCb',CrCb)

    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    cv2.imshow('Frame LAB',lab)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()