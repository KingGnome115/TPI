import cv2 #Importamos librerias
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./imagenes/Madotsuki.jpg',0) #Leemos la imagen
ret , thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #Umbralizamos la imagen Binaria
ret , thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) #Umbralizamos la imagen Binaria Inversa
ret , thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) #Umbralizamos la imagen Truncada
ret , thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) #Umbralizamos la imagen a cero
ret , thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) #Umbralizamos la imagen a cero Inversa

titles = ['original image','Binary','binary-inv','trunc','tozero','tozero-inv'] #Titulos
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5] #Imagenes

for i in range(6): 
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray') #Mostramos las imagenes
    plt.title(titles[i]) #Titulos
    plt.xticks([]),plt.yticks([]) #Eliminamos los ejes

plt.show()