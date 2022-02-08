import numpy as np #Para uso de calculos numericos ysu manejo
import cv2 #Para el tratamiento de imagenes

print("En este archivo cargaremos las imagenes")

img = cv2.imread('./imagenes/Madotsuki.jpg',1) #Cargamos la imagen
cv2.imshow('imagenRGB',img) #Mostramos la imagen
cv2.waitKey(0) #Esperamos a que se presione una tecla

img = cv2.imread('./imagenes/Madotsuki.jpg',0) #Cargamos la imagen
cv2.imshow('imagenGRAY',img) #Mostramos la imagen en grises
cv2.imwrite('./imagenes/MadotsukiGris.jpg',img) #Para guardar la imagen
cv2.waitKey(0) #Esperamos a que se presione una tecla


cv2.destroyAllWindows(0) #Destruimos todas las ventanas
