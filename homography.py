import matplotlib.pyplot as plt
import numpy as np
import cv2

#Cargamos la imagen deseada
img = cv2.imread("bandeja1.jpeg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img),plt.title('Original')

#Seleccionamos cuatro puntos
pts1 = np.float32([[400,380],[190,1200],[1510,400],[1800,1200]])

#Mostramos la imagen escalada
fig,ax = plt.subplots(1)
ax.imshow(img),plt.title('points')

#Dibujamos pts1 en la imagen escalada
for pts in pts1:
    circ = plt.Circle(pts,20)
    ax.add_patch(circ)


rows = img.shape[0]
cols = img.shape[1]

#Seleccionamos cuatro putnos de destino
pts2 = np.float32([[0,0],[0,rows],[cols,0],[cols,rows]])

#Se calcula la matriz para la correccion de perspectiva
M = cv2.getPerspectiveTransform(pts1,pts2)

#Obtenemos la imagen con correccion de pespectiva
img_hom = cv2.warpPerspective(img, M, (cols,rows))

#Mostramos la imagen resultante
fig1,ax1 = plt.subplots(1)
ax1.imshow(img_hom),plt.title('result')