import cv2

img = cv2.imread('./imagenes/DarkSouls.jpeg')# leer la imagen
cv2.imshow('Original', img)# mostrar la imagen original
edges1 = cv2.bitwise_not(cv2.Canny(img, 100, 200))# aplicar la función Canny para obtener los bordes
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# convertir la imagen a escala de grises
gray = cv2.medianBlur(gray, 5)# aplicar un filtro mediano para eliminar el ruido de la imagen
edges2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)# aplicar un filtro de umbralización adaptativo para obtener los bordes
dst = cv2.edgePreservingFilter(img, flags=2, sigma_s=64, sigma_r=0.25)# aplicar el filtro de restauración de bordes
cartoon1 = cv2.bitwise_and(dst, dst, mask=edges1)# aplicar la función bitwise AND para obtener la imagen en color
cartoon2 = cv2.bitwise_and(dst, dst, mask=edges2)# aplicar la función bitwise AND para obtener la imagen en color

cv2.imshow("Original", img)# mostrar la imagen original
cv2.imshow("Cartoon1", cartoon1)# mostrar la imagen en color
cv2.imshow("Cartoon2", cartoon2)# mostrar la imagen en color
cv2.waitKey(0)# esperar a que se presione una tecla

cv2.destroyAllWindows()# cerrar todas las ventanas