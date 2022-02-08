import matplotlib
import numpy as np #Para uso de calculos numericos ysu manejo
from matplotlib import pyplot as plt #matplotlib.pyplot sirve para graficar
import cv2 #Para el tratamiento de imagenes

img = cv2.imread('../imagenes/Nyarlathotep.webp',0) #Cargamos la imagen

ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #Binarizamos la imagen