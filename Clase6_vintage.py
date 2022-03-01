import cv2
import numpy as np

img = cv2.imread("./imagenes/Cyberpunk.jpg")# leer la imagen
original = img.copy()# copiar la imagen original
img = np.array(img, dtype=np.float64)# convertir la imagen a un array de 32 bits
img = cv2.transform(img, np.matrix([[0.272, 0.534, 0.131],
    [0.349, 0.686, 0.168],[0.393, 0.769, 0.189]]))# aplicar la transformación
img [np.where(img > 255)] = 255# obtener los valores menores a 255
img = np.array(img, dtype=np.uint8)# convertir la imagen a un array de 8 bits
cv2.imshow("Original", original)# mostrar la imagen original
cv2.imshow("Filtro", img)# mostrar la imagen filtrada
cv2.waitKey(0)# esperar a que se presione una tecla
cv2.destroyAllWindows()# cerrar todas las ventanas
