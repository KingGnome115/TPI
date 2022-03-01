import cv2
import numpy as np

img = cv2.imread("./imagenes/DarkSouls.jpeg",0)# leer la imagen
row, col = img.shape # obtener el número de filas y columnas de la imagen

negativo = np.zeros((row, col), dtype=np.uint8)# crear una matriz de ceros con el mismo tamaño de la imagen

for a in range(row):
    for b in range(col):
        negativo[a, b] = 255 - img[a, b] # obtener el valor negativo de cada pixel

cv2.imshow("Original", img)# mostrar la imagen original
cv2.imshow("Negativo", negativo)# mostrar la imagen negativa
cv2.waitKey(0)# esperar a que se presione una tecla
cv2.destroyAllWindows()# cerrar todas las ventanas