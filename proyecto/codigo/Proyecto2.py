# Autores: Jose Miguel Muñoz Ríos y Mauricio David Correa Hernádez
# código de compresión de imágenes.
# Trabajo: Entrega 2
# Semestre: 2021-02

import cv2 #opencv
from tkinter import * #interfaz grafica
from tkinter import filedialog
import os # crear carpetas y directorios desde python

directorio = filedialog.askdirectory()
nombreDelArchivo = os.listdir(directorio)

contador = 0
for lineaDeTexto in nombreDelArchivo:

    caminoAlArchivo = directorio + "/" + lineaDeTexto
    print(nombreDelArchivo)
    imagenOriginal = cv2.imread(caminoAlArchivo)

    carpetaNueva = "./carpetaDeImagenes"
    if not os.path.exists(carpetaNueva):
        os.makedirs(carpetaNueva)
    
    imagenFinal = cv2.resize(imagenOriginal, (1920, 1080), interpolation= cv2.INTER_NEAREST)
    cv2.imwrite(carpetaNueva+"/archivoFinal"+str(contador)+".jpg", imagenFinal)
    contador+=1
    print("/archivoFinal"+str(contador)+".jpg")