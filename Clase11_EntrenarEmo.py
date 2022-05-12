import cv2
import os
import numpy as np
import time

def obtenerModelo(method, faceData, labels):
    if method == 'EigenFace' : emotion_recognezer = cv2.face.EigenFaceRecognizer_create()
    if method == 'FisherFace': emotion_recognezer = cv2.face.FisherFaceRecognizer_create()
    if method == 'LBPHFace': emotion_recognezer = cv2.face.LBPHFaceRecognizer_create()

    #Entrenando el reconocimiento de rostros
    print("Entrenando reconocedor "+ method)

    inicio = time.time()
    emotion_recognezer.train(faceData , np.array(labels))
    fin = time.time() - inicio
    print("Tiempo de entrenamiento: ", fin)

    #Almacenar el modelo
    emotion_recognezer.write('modelo'+method+'.xml')
    print("Modelo almacenado")

dataPath = './Em'
emotionList = os.listdir(dataPath)
print("Lista de emociones: ", emotionList)
print(dataPath)

labels = []
faceData = []
label = 0

for nameDir in emotionList:
    emotionPath = dataPath + '/' + nameDir
    #print('Lista imagenes', personPath)
    for fileName in os.listdir(emotionPath):
        #print("Rostros", nameDir + ' ' + fileName)
        labels.append(label)
        faceData.append(cv2.imread(emotionPath+"/"+fileName))
        #print("path", personPath+"/"+fileName)
    label = label +1
obtenerModelo('EigenFace', faceData, labels)