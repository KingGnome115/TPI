import cv2
import numpy as np

captura = cv2.VideoCapture(0)
yelloBajo = np.array([15,100,20], np.uint8)
yelloAlto = np.array([45,255,255], np.uint8)

greenBajo = np.array([30,100,20], np.uint8)
greenAlto = np.array([80,255,255], np.uint8)

redBajo1 = np.array([0,100,20], np.uint8)
redAlto1 = np.array([180,255,255], np.uint8)

redBajo2 = np.array([175,100,20], np.uint8)
redAlto2 = np.array([179,255,255], np.uint8)

azulBajo = np.array([100,100,115], np.uint8)
azulAlto = np.array([120,255,255], np.uint8)

orangeBajo1=np.array([11,100,20], np.uint8)
orangeAlto1=np.array([19,255,255], np.uint8)

while(captura.isOpened()):
    ret, imagen = captura.read()
    if ret == True:
        frameSHV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) #Convertir a HSV
        maskYellow = cv2.inRange(frameSHV, yelloBajo, yelloAlto) #Crear mascara de color amarillo
        maskYellowvis = cv2.bitwise_and(imagen, imagen, mask=maskYellow) #Crear mascara de color amarillo visualizado
        maskGreen = cv2.inRange(frameSHV, greenBajo, greenAlto) #Crear mascara de color verde
        maskGreenvis = cv2.bitwise_and(imagen, imagen, mask=maskGreen) #Crear mascara de color verde visualizado
        maskRed = cv2.inRange(frameSHV, redBajo1, redAlto1) #Crear mascara de color rojo
        maskRedvis = cv2.bitwise_and(imagen, imagen, mask=maskRed) #Crear mascara de color rojo visualizado
        maskRed2 = cv2.inRange(frameSHV, redBajo2, redAlto2) #Crear mascara de color rojo
        maskRed2vid = cv2.bitwise_and(imagen, imagen, mask=maskRed2)
        maskBlue = cv2.inRange(frameSHV, azulBajo, azulAlto) #Crear mascara de color azul
        maskBluevis = cv2.bitwise_and(imagen, imagen, mask=maskBlue) #Crear mascara de color azul visualizado
        maskOrange = cv2.inRange(frameSHV, orangeBajo1, orangeAlto1) #Crear mascara de color naranja
        maskOrangevis = cv2.bitwise_and(imagen, imagen, mask=maskOrange) #Crear mascara de color naranja visualizado
        #unir mascaras en una sola
        mask = cv2.add(maskYellow, maskGreen)
        mask = cv2.add(mask, maskRed)
        mask = cv2.add(mask, maskRed2)
        mask = cv2.add(mask, maskBlue)
        mask = cv2.add(mask, maskOrange)
        #mostrar mask
        
        maskVis = cv2.bitwise_and(imagen, imagen, mask=mask)
        cv2.imshow('mask', maskVis)
        #cv2.imshow('maskYellowVis', maskYellowvis)
        #cv2.imshow('maskGreenVis', maskGreenvis)
        #cv2.imshow('maskRedVis', maskRedvis)
        #cv2.imshow('maskRed2Vis', maskRed2vid)
        #cv2.imshow('maskYellow', maskYellow)
        #cv2.imshow('maskGreen', maskGreen)
        #cv2.imshow('mas', mask)
        cv2.imshow('Camara', imagen)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: break
captura.release()
cv2.destroyAllWindows()
