
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pydicom
import os

class Paciente():
    pass
class DICOM():
    pass
import cv2

class IMAGENES: 
    def __init__(self, Ruta, ima):
        self.ruta = Ruta
        self.ima = ima

    def cargar_imagen(self):
        self.ima = cv2.imread(f"Imagenes/{self.ruta}")
        self.ima = cv2.cvtColor(self.ima, cv2.COLOR_BGR2RGB)


    def mostrar_imagen(self):
        if self.ima is not None:
            plt.imshow(self.ima)
            plt.axis("off")
            plt.show()
        else:
            print("Error: No se pudo cargar la imagen.")

    def binarizar_imagen(self, kernel, binarizacion):
        ima_gray = cv2.cvtColor(self.ima, cv2.COLOR_RGB2GRAY)
        # == Binarización de la imagen ==
        vmin = np.min(ima_gray)
        vmax = np.max(ima_gray)
        if binarizacion == 1:
            print("BINARIO")
            Umb,imgB=cv2.threshold(ima_gray,vmin,vmax,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            plt.imshow(imgB, cmap="gray")
            plt.show()
        elif binarizacion == 2:
            print("Binario invertido")
            Umb,imgB=cv2.threshold(ima_gray,vmin,vmax,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            plt.imshow(imgB, cmap="gray")
            plt.show()
        elif binarizacion == 3:
            print("Truncado")
            Umb,imgB=cv2.threshold(ima_gray,vmin,vmax,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
            plt.imshow(imgB, cmap="gray")
            plt.show()
        elif binarizacion == 4:
            print("Tozero")
            Umb,imgB=cv2.threshold(ima_gray,vmin,vmax,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
            plt.imshow(imgB, cmap="gray")
            plt.show()
        elif binarizacion == 5:
            print("Tozero invertido")
            Umb,imgB=cv2.threshold(ima_gray,vmin,vmax,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
            plt.imshow(imgB, cmap="gray")
            plt.show()




    
            