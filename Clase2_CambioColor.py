import cv2
import numpy as np

img = cv2.imread('./imagenes/Madotsuki.jpg',1)
cv2.imshow('imagenRGB',img)
cv2.waitKey(0)

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagenGRAY',gris)
cv2.waitKey(0)

hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('imagenHSV',hsv)
cv2.waitKey(0)

yuyv=cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow('imagenYUV',yuyv)
cv2.waitKey(0)

Tcrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('imagenYCrCb',Tcrcb)
cv2.waitKey(0)

b, g, r = cv2.split(img)
cv2.imshow('blue',b)
cv2.waitKey(0)
cv2.imshow('green',g)
cv2.waitKey(0)
cv2.imshow('red',r)
cv2.waitKey(0)

cv2.destroyAllWindows(0)