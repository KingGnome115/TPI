import cv2
import os
import numpy as np

dataPath = './fotos'
peopleList = os.listdir(dataPath)
print("Lista de personas: ", peopleList)
print(dataPath)

labels = []
faceData = []
label = 0

for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir
    #print('Lista imagenes', personPath)
    for fileName in os.listdir(personPath):
        #print("Rostros", nameDir + ' ' + fileName)
        labels.append(label)
        faceData.append(cv2.imread(personPath+"/"+fileName))
        #print("path", personPath+"/"+fileName)
    label = label +1

#Metodo de entrenamiento
#face_recognezer = cv2.face.LBPHFaceRecognizer_create()<-- no me funciono
#face_recognezer = cv2.face.EigenFaceRecognizer_create()
face_recognezer = cv2.face.FisherFaceRecognizer_create()


#Entrenar reconocedor
face_recognezer.train(faceData , np.array(labels))

#Almacenar modelo
face_recognezer.write('modeloFisherFace.xml')