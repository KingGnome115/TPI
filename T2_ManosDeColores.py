import cv2 #import cv2
from cv2 import bitwise_and
import numpy as np

def figColor(imageHSV):
    redBajo1 = np.array([0, 100, 20], np.uint8)
    redAlto1 = np.array([10, 255, 255], np.uint8)
    redBajo2 = np.array([175, 100, 20], np.uint8)
    redAlto2 = np.array([180, 255, 255], np.uint8)

    orangeBajo = np.array([11, 100, 20], np.uint8)
    orangeAlto = np.array([14, 255, 255], np.uint8)

    yellowBajo = np.array([15, 100, 20], np.uint8)
    yellowAlto = np.array([45, 255, 255], np.uint8)

    greenBajo = np.array([46, 100, 20], np.uint8)
    greenAlto = np.array([75, 255, 255], np.uint8)

    blueBajo = np.array([85, 100, 20], np.uint8)
    blueAlto = np.array([135, 255, 255], np.uint8)

    maskRed1 = cv2. inRange(imageHSV, redBajo1, redAlto1)
    maskRed2 = cv2. inRange(imageHSV, redBajo2, redAlto2)
    maskRed = cv2. add(maskRed1, maskRed2)
    maskOrange = cv2. inRange(imageHSV, orangeBajo, orangeAlto)
    maskYellow = cv2. inRange(imageHSV, yellowBajo, yellowAlto)
    maskGreen = cv2. inRange(imageHSV, greenBajo, greenAlto)
    maskBlue = cv2. inRange(imageHSV, blueBajo, blueAlto)

    contornoRed, _ = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornoOrange, _ = cv2.findContours(maskOrange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornoYellow, _ = cv2.findContours(maskYellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornoGreen, _ = cv2.findContours(maskGreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornoBlue, _ = cv2.findContours(maskBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    textColor = ' ' + '| Color: '
    if len(contornoRed) > 0:
        textColor = ' ' + 'Rojo'
    elif len(contornoOrange) > 0:
        textColor = ' ' + 'Naranja'
    elif len(contornoYellow) > 0:
        textColor = ' ' + 'Amarillo'
    elif len(contornoGreen) > 0:
        textColor = ' ' + 'Verde'
    elif len(contornoBlue) > 0:
        textColor = ' ' + 'Azul'
    return textColor

def figName(contorno):
    nombreFiguraTmp = 'Forma: '
    nombreFigura = nombreFiguraTmp + ' '
    epsilon = 0.01 * cv2.arcLength(contorno, True)
    approx = cv2.approxPolyDP(contorno, epsilon, True)
    nombreFigura = figMasLineas(contorno)
    return [nombreFigura, approx]

def figMasLineas(contorno):
    nombreFiguraTmp = 'Forma: '
    nombreFigura = nombreFiguraTmp + 'error'
    # valor que se cambia y valor de margen de error | sacar la longitud del contorno
    epsilon = float(0.1e-3) * cv2.arcLength(contorno, True)
    # Valor aproximado : contorno | valor a cambiar | Que sea mas aproximaod al resultado
    approx = cv2.approxPolyDP(contorno, epsilon, True) # contorno, epsilon, True
    if len(approx) >= 401:
        nombreFigura = nombreFiguraTmp + 'Mano '
    return nombreFigura + str(len(approx))

image = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(image.isOpened()): #Mientras la camara este abierta
    ret, imagen = image.read()
    if ret == True:
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) #Convertir a escala de grises
        canny = cv2.Canny(gray, 10, 150) #Deteccion de bordes
        canny = cv2.dilate(canny, None, iterations=1) #Dilatacion
        canny = cv2.erode(canny, None, iterations=1)#Erosion
        contornos, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Deteccion de contornos
        imageHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)#Convertir a HSV

        for c in contornos:
            x, y, w, h = cv2.boundingRect(c) #Obtener el rectangulo que engloba el contorno
            imgAux = np.zeros(imagen.shape[:2], dtype='uint8') #Crear una imagen auxiliar
            imgAux = cv2.drawContours(imgAux, [c], -1, 255, -1) #Dibujar el contorno en la imagen auxiliar
            maskHSV = bitwise_and(imageHSV, imageHSV, mask=imgAux) #Obtener la mascara de la imagen auxiliar
            figAll=figName(c) #Obtener el nombre de la figura
            textoFig = figAll[0]+figColor(maskHSV) #Obtener el nombre de la figura y el color
            cv2.putText(imagen, textoFig, (x, y-5), 1, 1, (52, 55, 52), 1) #Escribir el nombre de la figura
            cv2.drawContours(imagen, [figAll[1]], 0, (0, 255, 0), 2) #Dibujar el contorno de la figura

        cv2.imshow('imagen', imagen)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

image.release()
cv2.destroyAllWindows()