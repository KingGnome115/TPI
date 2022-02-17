import cv2
import numpy as np

captura = cv2.VideoCapture(0)
yelloBajo = np.array([0,100,5], np.uint8)
yelloAlto = np.array([10,255,255], np.uint8)

while(captura.isOpened()):
    ret, imagen = captura.read()
    if ret == True:
        frameSHV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) #Convertir a HSV
        maskYellow = cv2.inRange(frameSHV, yelloBajo, yelloAlto) #Crear mascara de color amarillo
        maskYellowvis = cv2.bitwise_and(imagen, imagen, mask=maskYellow) #Crear mascara de color amarillo visualizado
        cv2.imshow('maskYellowVis', maskYellowvis)
        cv2.imshow('maskYellow', maskYellow)
        cv2.imshow('Camara', imagen)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: break
captura.release()
cv2.destroyAllWindows()
