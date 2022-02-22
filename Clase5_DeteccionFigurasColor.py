import cv2
import numpy as np

def figColor(imageHSV):
	
	#Colores a Detectar
	#Valores de Rojo parte baja
	redBajo1=np.array([0,100,20], np.uint8)
	redAlto1=np.array([10,255,255], np.uint8)
	#Valores de Rojo parte alta
	redBajo2=np.array([175,100,20], np.uint8)
	redAlto2=np.array([180,255,255], np.uint8)

	#Valores de Naranja parte baja
	orangeBajo1=np.array([11,100,20], np.uint8)
	orangeAlto1=np.array([19,255,255], np.uint8)

	#Valores de Amarillo parte baja
	yellowBajo1=np.array([15,100,20], np.uint8)
	yellowAlto1=np.array([45,255,255], np.uint8)

	#Valores de Verde parte baja
	greenBajo1=np.array([36,100,20], np.uint8)
	greenAlto1=np.array([70,255,255], np.uint8)

	#Valores de Violeta parte baja
	violetBajo1=np.array([130,100,20], np.uint8)
	violetAlto1=np.array([145,255,255], np.uint8)

	#Valores de Rosa parte baja
	pinkBajo1=np.array([146,100,20], np.uint8)
	pinkAlto1=np.array([170,255,255], np.uint8)

	#Valores de Azul parte baja
	blueBajo1=np.array([100,100,20], np.uint8)
	blueAlto1=np.array([125,255,255], np.uint8)

	#se buscan los colores de la imagen de acuerdo a sus limites
	maskRed1 = cv2.inRange(imageHSV,redBajo1,redAlto1)
	maskRed2 = cv2.inRange(imageHSV,redBajo2,redAlto2)
	maskRed = cv2.add(maskRed1,maskRed2)
	maskOrange = cv2.inRange(imageHSV,orangeBajo1,orangeAlto1)
	maskYellow = cv2.inRange(imageHSV,yellowBajo1,yellowAlto1)
	maskGreen = cv2.inRange(imageHSV,greenBajo1,greenAlto1)
	maskViolet = cv2.inRange(imageHSV,violetBajo1,violetAlto1)
	maskPink = cv2.inRange(imageHSV,pinkBajo1,pinkAlto1)
	maskBlue = cv2.inRange(imageHSV,blueBajo1,blueAlto1)

	#Deteccion de los colores en la imagen
	#contornos, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsRed, _ = cv2.findContours(maskRed,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsOrange, _ = cv2.findContours(maskOrange,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsYellow, _ = cv2.findContours(maskYellow,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsGreen, _ = cv2.findContours(maskGreen,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsViolet, _ = cv2.findContours(maskViolet,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsPink, _ = cv2.findContours(maskPink,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsBlue, _ = cv2.findContours(maskBlue,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	color='x'

	#Etiquetado de color
	if len(cntsRed)>0: color='Rojo'
	elif len(cntsOrange)>0: color='Naranja'
	elif len(cntsYellow)>0: color='Amarillo'
	elif len(cntsGreen)>0: color='Verde'
	elif len(cntsViolet)>0: color='Violeta'
	elif len(cntsPink)>0: color='Rosa'
	elif len(cntsBlue)>0: color='Azul'

	return color




def figName(contorno, width,heigth):
	nameFig='x'
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

image = cv2.imread('./imagenes/Madotsuki.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10,150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
contornos, _ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
for c in contornos:
	x,y,w,h = cv2.boundingRect(c)
	imAux = np.zeros(image.shape[:2], dtype='uint8')
	imAux = cv2.drawContours(imAux,[c],-1,255,-1)
	maskHSV = cv2.bitwise_and(imageHSV, imageHSV, mask = imAux)
	figAll = figName(c,w,h) + ' ' + figColor(maskHSV)
	cv2.putText(image,figAll,(x,y-5),1,1,(0,255,0),1)

cv2.imshow('imagen',image)
cv2.imshow('canny',canny)
cv2.imshow('imagenHSV',imageHSV)
cv2.waitKey(0)
cv2.destroyAllWindows()
