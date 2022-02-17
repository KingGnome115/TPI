import cv2
import numpy as np 
from matplotlib import pyplot as plt 

#Leemos la imagen a color con 1 y en escala de grises con 0
img = cv2.imread('./imagenes/Madotsuki.jpg', 1)

#Transformamos de RGB a los espacios/modelos de color
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #Modelo de color XYZ
luv = cv2.cvtColor(img, cv2.COLOR_RGB2LUV)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
bgr = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
yuv = cv2.cvtColor(img, cv2.COLOR_RGBA2YUV_I420)

#Comenzamos a generar el plot
#Hacemos un arreglo con las imagenes
imagenes = [gray, 0 ,luv, 0 ,hsv, 0 ,bgr, 0 ,yuv, 0]

#Le ponemos titulos a las imagenes que vamos a mostrar
tittle = ['Gray', 'HISTOGRAMA' ,'LUV', '' ,'HSV', '' ,'BGR', '' ,'YUV I420', '']

#Definimos las pocisiones del arreglo 
miArray = np.arange(5)

#Comenzamos a recorrer el arreglo
for i in miArray:
    plt.subplot(5,2,i*2+1),plt.imshow(imagenes[i*2],'gray')
    plt.title(tittle[i*2]),plt.xticks([]),plt.yticks([])

    plt.subplot(5,2,i*2+2),plt.hist(imagenes[i*2].ravel(),360)
    plt.title(tittle[i*2+1]),plt.xticks([]),plt.yticks([])

#Mostramos las imagenes 
plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows(0)