import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

img = 0
espejo = 0
verde = 0
cartoonr = 0
cartoonrVerde = 0

while(cap.isOpened()):
    ret, imagen = cap.read()
    re2, imagen2 = cap.read()
    ret3, imagen3 = cap.read() 
    if ret == True:
        frameSHV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV) #Modelo de color HSV para el color rojo
        
        cv2.imshow('Video', imagen)# Mostramos la imagen
        img = imagen
        #Filtro espejo        
        anchoMitad = imagen2.shape[1] // 2 #ancho de la imagen dividido entre 2
        imagen2[:,:anchoMitad] = cv2.flip(imagen2[:,anchoMitad:],1) #Espejo de la mitad de la imagen
        cv2.imshow('Espejo',imagen2) #Mostramos la imagen espejo
        espejo = imagen2
        #Filtro verde
        imagen3[:, :, 0] = 0 #Ponemos todo el canal 0 a 0
        imagen3[:, :, 2] = 0 #Ponemos todo el canal 2 a 0
        cv2.imshow("Canal verde", imagen3)#Mostramos la imagen verde
        verde = imagen3
        #Caricatura
        edges1 = cv2.bitwise_not(cv2.Canny(imagen, 100, 200)) #Convertimos la imagen a escala de grises y aplicamos el filtro de canny
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) #Convertimos la imagen a escala de grises
        gray1 = cv2.medianBlur(gray, 5)#Aplicamos el filtro de mediana
        dst = cv2.edgePreservingFilter(imagen, flags=2, sigma_r=0.25, sigma_s=64 )#Aplicamos el filtro de edgePreservingFilter
        cartoon = cv2.bitwise_and(dst, dst, mask=edges1)#Aplicamos el filtro de mascara
        cv2.imshow('Cartoon', cartoon)#Mostramos la imagen cartoon
        cartoonr = cartoon
        #Caricatura radioactiva
        imagen3[:, :, 0] = 0
        imagen3[:, :, 2] = 0
        edges1_2 = cv2.bitwise_not(cv2.Canny(imagen3, 100, 200))#Convertimos la imagen a escala de grises y aplicamos el filtro de canny
        gray_2 = cv2.cvtColor(imagen3, cv2.COLOR_BGR2GRAY)#Convertimos la imagen a escala de grises
        gray1_2 = cv2.medianBlur(gray_2, 5)#Aplicamos el filtro de mediana 
        dst_2 = cv2.edgePreservingFilter(imagen3, flags=2, sigma_r=0.25, sigma_s=64 )#Aplicamos el filtro de edgePreservingFilter
        cartoon2 = cv2.bitwise_and(dst_2, dst_2, mask=edges1_2)#Aplicamos el filtro de mascara
        cv2.imshow('Cartoon_Verde', cartoon2)#Mostramos la imagen cartoon
        cartoonrVerde = cartoon2

        hist1 = cv2.calcHist([espejo], [0], None, [256], [0, 256])#Calculamos el histograma de la imagen
        hist2 = cv2.calcHist([verde], [0], None, [256], [0, 256])#Calculamos el histograma de la imagen
        hist3 = cv2.calcHist([cartoonr], [0], None, [256], [0, 256])#Calculamos el histograma de la imagen
        hist4 = cv2.calcHist([cartoonrVerde], [0], None, [256], [0, 256])#Calculamos el histograma de la imagen
        plt.plot(hist1)#Mostramos el histograma
        plt.plot(hist2)#Mostramos el histograma
        plt.plot(hist3)#Mostramos el histograma
        plt.plot(hist4)#Mostramos el histograma
        plt.show()#Mostramos el histograma
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: break
cv2.destroyAllWindows()