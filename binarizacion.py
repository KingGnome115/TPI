import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('./imagenes/Madotsuki.jpg', 0)

#Binarizacion: Cargar en un rango de pixeles 
#Parametros de threshold
#El archivo
#El rangoo (Cantidad de pixeles)
#Hasta que tamaño el maximo rango
#Para hacer la binarizacion 
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#Usar filtro
blur = cv2.GaussianBlur(img, (5,5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#Generar un plot de las imagenes
#Se genera un arreglo con las caracteristicas
imagenes = [img, 0, th1, img, 0, th2, blur, 0, th3]

#Le damos titulos a cada imagen
titles = ['Original', 'Histograma', 'THR 127', 
'Original', 'Histograma', 'OSTU', 
'Filtro Gaussiano', 'Histograma', 'OTSU']   

#Asociamos a Numpy con el arreglo de arriba
miArray = np.arange(3)

#Ejecutamos el arreglo
for i in miArray:
    plt.subplot(3,3,i*3+1), plt.imshow(imagenes[i*3],'gray') 
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])

    plt.subplot(3,3,i*3+2), plt.hist(imagenes[i*3].ravel(), 256) 
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([]) 
    
    plt.subplot(3,3,i*3+3), plt.imshow(imagenes[i*3+2],'gray') 
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([]) 
plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows(0)