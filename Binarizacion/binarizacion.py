import matplotlib
import numpy as np #Para uso de calculos numericos ysu manejo
from matplotlib import pyplot as plt #matplotlib.pyplot sirve para graficar
import cv2 #Para el tratamiento de imagenes

img = cv2.imread('../imagenes/Nyarlathotep.webp',0) #Cargamos la imagen

#Como trabajamos en matrices, debemos convertir la imagen a matriz
#ret1 es una matriz con la imagen en grises
#th1 es una matriz con la imagen binarizada
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #Binarizamos la imagen

ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Binarizamos la imagen

blur = cv2.GaussianBlur(img, (5,5), 0) #Aplicamos un filtro gaussiano

ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Binarizamos la imagen

imagenes = [img, 0, th1, img, 0, th2, blur, 0, th3] #Creamos una lista con las imagenes

#Creamos una lista con los titulos de las imagenes
titles = ['Original', 'Histograma', 'THR 127',
'Original', 'Histograma', 'OTSU',
'Filtro Gaussiano', 'Histograma', 'OTSU']

miArray = np.arange(3)  #Creamos una matriz de 3 filas y 3 columnas

for i in miArray: #Recorremos la matriz
    plt.subplot(3,3,i*3+1), plt.imshow(imagenes[i*3], 'gris') #Creamos una subplota
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([]) #Creamos un titulo para la subplota

    plt.subplot(3,3,i*3+2), plt.hist(imagenes[i*3+1].ravel(), 256) #Creamos un histograma
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([]) #Creamos un titulo para el histograma 

    plt.subplot(3,3,i*3+3), plt.imshow(imagenes[i*3+2], 'gray') #Creamos una subplota
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([]) #Creamos un titulo para la subplota

plt.show() #Mostramos el grafico