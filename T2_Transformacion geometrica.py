#Importamos librerias
import cv2
import numpy as np

#Leemos la imagem
src = cv2.imread('./imagenes/Madotsuki.jpg')
rows, cols = src.shape[:2]
#Rotamos la kamgen 
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
dst = cv2.warpAffine(src, M, (cols, rows))
#Se muestra 
cv2.imshow('Imagen', src)
cv2.imshow('Rotacion', dst)
cv2.waitKey()