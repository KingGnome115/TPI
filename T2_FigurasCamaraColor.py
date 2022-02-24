import cv2
import numpy as np

captura = cv2.VideoCapture(0)

def figColor(imageHSV):
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

	#se buscan los colores de la imagen de acuerdo a sus limites
	maskRed1 = cv2.inRange(imageHSV,redBajo1,redAlto1)
	maskRed2 = cv2.inRange(imageHSV,redBajo2,redAlto2)
	maskRed = cv2.add(maskRed1,maskRed2)
	maskOrange = cv2.inRange(imageHSV,orangeBajo1,orangeAlto1)
	maskYellow = cv2.inRange(imageHSV,yelloBajo,yelloAlto)
	maskGreen = cv2.inRange(imageHSV,greenBajo,greenAlto)
	maskBlue = cv2.inRange(imageHSV,azulBajo,azulAlto)

	#Deteccion de los colores en la imagen
	#contornos, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsRed, _ = cv2.findContours(maskRed,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsOrange, _ = cv2.findContours(maskOrange,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsYellow, _ = cv2.findContours(maskYellow,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsGreen, _ = cv2.findContours(maskGreen,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsBlue, _ = cv2.findContours(maskBlue,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	color=''

	#Etiquetado de color
	if len(cntsRed)>0: color='Rojo'
	elif len(cntsOrange)>0: color='Naranja'
	elif len(cntsYellow)>0: color='Amarillo'
	elif len(cntsGreen)>0: color='Verde'
	elif len(cntsBlue)>0: color='Azul'

	return color


def figName(contorno, width,heigth):
	nameFig=''
	epsilon = 0.01 * cv2.arcLength(contorno,True)#Cambiar el porcentaje de epsilon
	approx= cv2.approxPolyDP(contorno,epsilon,True)
	#Etiquetar cada figura
	if len(approx)==3:
		nameFig ='Triangulo'

	if len(approx)==4:
		aspect_ratio = float(width)/heigth
		if aspect_ratio >= 1:
			nameFig ='Cuadrado'
		else:
			nameFig ='Rectangulo'

	if len(approx)==5:
		nameFig ='Pentagono'

	if len(approx)==6:
		nameFig ='Hexagono'

	if len(approx)>10:
		nameFig ='Circulo'

	return nameFig

#Detectar figuras y color en la camara
while(captura.isOpened()):
    ret, imagen = captura.read()
    if ret == True:
        #tomar un frame con los colores originales
        frame = imagen.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray,10,150)
        canny = cv2.dilate(canny, None, iterations=1)
        canny = cv2.erode(canny, None, iterations=1)
        contornos, _ = cv2.findContours(canny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        imageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        for cnt in contornos:
            x, y, w, h = cv2.boundingRect(cnt)
            imAux = np.zeros(frame.shape[:2], dtype='uint8')
            imAux = cv2.drawContours(imAux, [cnt], -1, 255, -1)
            maskHSV = cv2.bitwise_and(imageHSV, imageHSV, mask=imAux)
            figAll = figName(cnt, w, h) + ' ' + figColor(maskHSV)
            cv2.putText(frame,figAll,(x,y-5),1,1,(0,255,0),1)


        cv2.imshow('Camara',frame)
        cv2.imshow('Canny',canny)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
captura.release()
cv2.destroyAllWindows()