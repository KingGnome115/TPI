import numpy as np #Importamos librerias 
import cv2 
from matplotlib import pyplot as plt 

img = cv2.imread('./imagenes/Madotsuki.jpg') #Leemos la imagen 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convertimos a escala de grises

ret, thresh = cv2.threshold(gray, 0, 255, #Umbralizamos la imagen
    cv2.THRESH_BINARY_INV + #Umbralizacion binaria inversa
    cv2.THRESH_OTSU) #Umbralizacion binaria inversa
cv2.imshow('SEGMENTACION', thresh) #Mostramos la imagen

cv2.waitKey(0)
cv2.destroyAllWindows()