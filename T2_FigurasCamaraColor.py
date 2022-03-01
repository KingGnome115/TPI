import cv2
import numpy as np

captura = cv2.VideoCapture(0)#Captura de imagen de la camara

def figColor(imageHSV):
	yelloBajo = np.array([15,100,20], np.uint8)#Definir los rangos bajos de color para el amarillo
	yelloAlto = np.array([45,255,255], np.uint8)#Definir los rangos altos de color para el amarillo

	greenBajo = np.array([30,100,20], np.uint8)#Definir los rangos bajos de color para el verde
	greenAlto = np.array([80,255,255], np.uint8)#Definir los rangos altos de color para el verde

	redBajo1 = np.array([0,99,20], np.uint8)#Definir los rangos bajos de color para el rojo
	redAlto1 = np.array([180,255,255], np.uint8)#Definir los rangos altos de color para el rojo

	redBajo2 = np.array([175,100,20], np.uint8)#Definir los rangos bajos de color para el rojo
	redAlto2 = np.array([179,255,255], np.uint8)#Definir los rangos altos de color para el rojo

	azulBajo = np.array([100,100,115], np.uint8)#Definir los rangos bajos de color para el azul
	azulAlto = np.array([120,255,255], np.uint8)#Definir los rangos altos de color para el azul

	orangeBajo1=np.array([11,100,20], np.uint8)#Definir los rangos bajos de color para el naranja
	orangeAlto1=np.array([19,255,255], np.uint8)#Definir los rangos altos de color para el naranja

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


def figName(contorno, width, heigth):
	nameFig=''
	epsilon = 0.03 * cv2.arcLength(contorno,True)#Cambiar el porcentaje de epsilon para cambiar la precision de la aproximacion
	approx= cv2.approxPolyDP(contorno,epsilon,True)#Aproximacion del contorno
	#Etiquetar cada figura
	if len(approx)==3:
		nameFig ='Triangulo'

	if len(approx)==4:
		aspect_ratio = float(width)/heigth
		if aspect_ratio <= 1:
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
while(captura.isOpened()):#Mientras la camara este abierta
    ret, imagen = captura.read()#Leer la imagen de la camara
    if ret == True:#Si la imagen se leyo correctamente se continua
        #tomar un frame con los colores originales
        frame = imagen.copy()#Copiar la imagen original en un frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#Convertir la imagen a escala de grises
        canny = cv2.Canny(gray,10,150)#Detectar bordes con Canny y umbrales de 10 y 150
        canny = cv2.dilate(canny, None, iterations=1)#Dilatar los bordes para eliminar los bordes pequeños
        canny = cv2.erode(canny, None, iterations=1)#Erode los bordes para eliminar los bordes grandes
        contornos, _ = cv2.findContours(canny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#Buscar los contornos
        imageHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#Convertir la imagen a HSV

        for cnt in contornos:#Recorrer los contornos encontrados
            x, y, w, h = cv2.boundingRect(cnt)#Obtener los limites de los contornos encontrados
            imAux = np.zeros(frame.shape[:2], dtype='uint8')#Crear una imagen auxiliar para dibujar los contornos
            imAux = cv2.drawContours(imAux, [cnt], -1, 255, -1)#Dibujar los contornos encontrados en la imagen auxiliar
            maskHSV = cv2.bitwise_and(imageHSV, imageHSV, mask=imAux)#Obtener la parte de la imagen que esta en el contorno
            figAll = figName(cnt, w, h) + ' ' + figColor(maskHSV)#Obtener el nombre de la figura y el color de la figura
            cv2.putText(frame,figAll,(x,y-5),1,1,(0,255,0),1)#Escribir el nombre de la figura y el color en la imagen

        cv2.imshow('Camara',frame)#Mostrar la imagen con los contornos y los colores
        cv2.imshow('Canny',canny)#Mostrar la imagen con los bordes detectados

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
captura.release()
cv2.destroyAllWindows()