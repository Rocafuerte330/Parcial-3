
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

    def binarizar_imagen(self, binarizacion, kernel, dibujo, Ruta):
        ima_gray = cv2.cvtColor(self.ima, cv2.COLOR_RGB2GRAY)
        # == Binarización de la imagen ==
        vmin = np.min(ima_gray)
        vmax = np.max(ima_gray)
        if binarizacion == 1:
            Umb,imgB=cv2.threshold(ima_gray,vmin,vmax,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        elif binarizacion == 2:
            Umb,imgB=cv2.threshold(ima_gray,vmin,vmax,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        elif binarizacion == 3:
            Umb,imgB=cv2.threshold(ima_gray,vmin,vmax,cv2.THRESH_TRUNC+cv2.THRESH_OTSU)
        elif binarizacion == 4:
            Umb,imgB=cv2.threshold(ima_gray,vmin,vmax,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
        elif binarizacion == 5:
            Umb,imgB=cv2.threshold(ima_gray,vmin,vmax,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
        else:
            print("Valor no válido")
        
        imaT=cv2.morphologyEx(imgB, cv2.MORPH_CLOSE, kernel, iterations = 4)

        a = np.shape(imaT)
        Y = int(a[0]/2)
        Y1 = Y - 150
        Y2 = Y + 150
        X = int(a[1]/2)
        X1 = X - 200
        X2 = X +200
        Punto_inicio = (X1,Y1)
        Punto_final = (X2,Y2)

        if dibujo == 1:
            plt.figure(figsize=(16,6))
            plt.subplot(1,3,1)
            plt.imshow(self.ima)
            plt.title("Imagen original")

            plt.subplot(1,3,2)
            plt.imshow(imaT, cmap="gray")
            plt.title("Imagen sin dibujo")

            ima_rec = cv2.rectangle(imaT,Punto_inicio, Punto_final,(12, 100, 255), -4)
            cv2.putText(imaT, "Imagen Binarizada", (X1,Y1+35), cv2.FONT_ITALIC, 1, (14,242,97), 4, cv2.LINE_AA)
            cv2.putText(imaT, f"Umb: {Umb}", (X1,Y), cv2.FONT_ITALIC, 1, (14,242,97), 4, cv2.LINE_AA)
            cv2.putText(imaT, f"Kernel: {kernel}", (X1,Y2-15), cv2.FONT_ITALIC, 1, (14,242,97), 4, cv2.LINE_AA)

            plt.subplot(1,3,3)
            plt.imshow(ima_rec)
            plt.title("Imagen con dibujo")
            plt.show()

        elif dibujo == 2:
            plt.figure(figsize=(16,6))
            plt.subplot(1,3,1)
            plt.imshow(self.ima)
            plt.title("Imagen original")

            plt.subplot(1,3,2)
            plt.imshow(imaT, cmap="gray")
            plt.title("Imagen sin dibujo")

            ima_cir = cv2.circle(imaT, (X,Y), 200, (12, 100, 255), -4)
            cv2.putText(imaT, "Imagen Binarizada", (X1,Y1+35), cv2.FONT_ITALIC, 1, (14,242,97), 4, cv2.LINE_AA)
            cv2.putText(imaT, f"Umb: {Umb}", (X1,Y), cv2.FONT_ITALIC, 1, (14,242,97), 4, cv2.LINE_AA)
            cv2.putText(imaT, f"Kernel: {kernel}", (X1,Y2-15), cv2.FONT_ITALIC, 1, (14,242,97), 4, cv2.LINE_AA)

            plt.subplot(1,3,3)
            plt.imshow(ima_cir)
            plt.title("Imagen con dibujo")
            plt.show()
 
        else:
            print("Valor no válido")

    def gaurdar_imagen():
        pass



    
            