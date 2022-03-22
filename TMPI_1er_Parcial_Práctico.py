from tkinter import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, imagen = cap.read()
    re2, imagen2 = cap.read()
    ret3, imagen3 = cap.read()
    if ret == True:
        frameSHV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
        
        cv2.imshow('Video', imagen)
        
        #-------------Espejo-----------------        
        anchoMitad = imagen2.shape[1] // 2
        imagen2[:,:anchoMitad] = cv2.flip(imagen2[:,anchoMitad:],1)
        cv2.imshow('Espejo',imagen2)
        #------------FIN ESPEJO------------------
                
        #----------------FILTRO VERDE-------------
        
        imagen3[:, :, 0] = 0
        imagen3[:, :, 2] = 0
        cv2.imshow("Canal verde", imagen3)
        
        #-----------------FIN FILTRO VERDE----------
        
        #-----------------CARICATURA----------
        edges1 = cv2.bitwise_not(cv2.Canny(imagen, 100, 200))
        #cambiar a grises para obtener caracteristicas
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.medianBlur(gray, 5)
        #mascara para diferencias en los edges, matriz de 7*7
        dst = cv2.edgePreservingFilter(imagen, flags=2, sigma_r=0.25, sigma_s=64 )
        cartoon = cv2.bitwise_and(dst, dst, mask=edges1)
        cv2.imshow('Cartoon', cartoon)
        #---------FIN CARICATURA------------------

        #-----------------CARICATURA----------

        imagen3[:, :, 0] = 0
        imagen3[:, :, 2] = 0
        edges1_2 = cv2.bitwise_not(cv2.Canny(imagen3, 100, 200))
        #cambiar a grises para obtener caracteristicas
        gray_2 = cv2.cvtColor(imagen3, cv2.COLOR_BGR2GRAY)
        gray1_2 = cv2.medianBlur(gray_2, 5)
        #mascara para diferencias en los edges, matriz de 7*7
        dst_2 = cv2.edgePreservingFilter(imagen3, flags=2, sigma_r=0.25, sigma_s=64 )
        cartoon2 = cv2.bitwise_and(dst_2, dst_2, mask=edges1_2)
        cv2.imshow('Cartoon_Verde', cartoon2)
        
        #---------FIN CARICATURA------------------
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: break
cap.realse()

cv2.destroyAllWindows()


##############/////////////////////////////******


