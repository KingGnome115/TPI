import cv2
import os

dataPath = './fotos'
peopledataPath = './fotos'
peopleList = os.listdir(dataPath)

#Metodo de entrenamiento
face_recognezer = cv2.face.LBPHFaceRecognizer_create()

#lectura del modelo
face_recognezer.read('modeloLBPHFace.xml')


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

d=''