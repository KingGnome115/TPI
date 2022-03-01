import cv2
import numpy as np

img = cv2.imread("./imagenes/DarkSouls.jpeg")# leer la imagen
dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.09, shade_factor=0.04)# aplicar el filtro

cv2.imshow("Original", img)# mostrar la imagen original
cv2.imshow("Filtro", dst_color)# mostrar la imagen filtrada
cv2.imshow("Negativo", dst_gray)# mostrar la imagen negativa

cv2.waitKey(0)# esperar a que se presione una tecla
cv2.destroyAllWindows()# cerrar todas las ventanas
