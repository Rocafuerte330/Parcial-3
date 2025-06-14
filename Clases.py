
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pydicom
import os

class Paciente:
    def __init__(self, nombre, edad, ID, imagen):
        self.nombre = nombre
        self.edad = edad
        self.ID = ID
        self.imagen = imagen  

    def __str__(self):
        return f"Paciente: {self.nombre}, Edad: {self.edad}, ID: {self.ID}, Volumen: {self.imagen.shape}"

def cargar_carpeta_dicom(ruta_carpeta):
    archivos = [pydicom.dcmread(os.path.join(ruta_carpeta, f)) 
                for f in os.listdir(ruta_carpeta) if f.endswith('.dcm')]    
    return archivos

def reconstruir_volumen(archivos_dicom):
    volumen = np.stack([f.pixel_array for f in archivos_dicom], axis=0)
    return volumen

def mostrar_cortes(volumen_3d):
    corte_transversal = volumen_3d[volumen_3d.shape[0] // 2, :, :]
    corte_coronal = volumen_3d[:, volumen_3d.shape[1] // 2, :]
    corte_sagital = volumen_3d[:, :, volumen_3d.shape[2] // 2]

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    axs[0].imshow(corte_transversal, cmap='gray')
    axs[0].set_title('Corte Transversal (Axial)')

    axs[1].imshow(corte_coronal, cmap='gray')
    axs[1].set_title('Corte Coronal')

    axs[2].imshow(corte_sagital, cmap='gray')
    axs[2].set_title('Corte Sagital')

    for ax in axs:
        ax.axis('off')

    plt.tight_layout()
    plt.savefig("3_Cortes.png")
    plt.show()


def crear_paciente(archivos_dicom, volumen_3d):
    dicom = archivos_dicom[0]
    nombre = dicom.PatientName
    edad = dicom.PatientAge
    ID = dicom.PatientID
    return Paciente(nombre, edad, ID, volumen_3d)

def aplicar_traslacion_corte_transversal(volumen_3d):
    # Tomar corte axial central
    corte = volumen_3d[volumen_3d.shape[0] // 2, :, :]

    # Opciones predeterminadas
    opciones = {
        "1": (30, 30),
        "2": (-30, 20),
        "3": (50, -20),
        "4": (-50, -30)
    }
    print("\nOpciones de traslación:")
    for k, (dx, dy) in opciones.items():
        print(f"{k}: dx = {dx}, dy = {dy}")

    eleccion = input("Seleccione una opción [1-4]: ")
    dx, dy = opciones.get(eleccion, (0, 0))

    # Aplicar traslación
    filas, columnas = corte.shape
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    trasladada = cv2.warpAffine(corte, M, (columnas, filas))

    # Mostrar y guardar comparación
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))
    axs[0].imshow(corte, cmap='gray')
    axs[0].set_title('Corte Axial Original')
    axs[1].imshow(trasladada, cmap='gray')
    axs[1].set_title(f'Traslación: dx={dx}, dy={dy}')
    for ax in axs:
        ax.axis('off')
    plt.tight_layout()

    # Guardar figura completa
    nombre_figura = f"comparacion_original_vs_trasladada_dx{dx}_dy{dy}.png"
    plt.savefig(nombre_figura)
    print(f" Comparación guardada como: {nombre_figura}")

    plt.show()




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

    def binarizar_imagen(self, binarizacion, kernel, dibujo, clave):
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


        imaEro = cv2.erode(imgB,kernel,iterations = 50)
        imaT = cv2.dilate(imaEro,kernel,iterations = 10)

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

            ima_rec = cv2.rectangle(imaT,Punto_inicio, Punto_final,(255, 255, 255), -4)
            cv2.putText(imaT, "Imagen Binarizada", (X1,Y1+35), cv2.FONT_ITALIC, 1, (0,0,0), 4, cv2.LINE_AA)
            cv2.putText(imaT, f"Umb: {Umb}", (X1,Y), cv2.FONT_ITALIC, 1, (0,0,0), 4, cv2.LINE_AA)
            cv2.putText(imaT, f"Kernel: {kernel}", (X1,Y2-15), cv2.FONT_ITALIC, 1, (0,0,0), 4, cv2.LINE_AA)

            plt.subplot(1,3,3)
            plt.imshow(ima_rec)
            plt.title("Imagen con dibujo")

            plt.savefig(f"{clave} binarizada.png")
            plt.show()

        elif dibujo == 2:
            plt.figure(figsize=(16,6))
            plt.subplot(1,3,1)
            plt.imshow(self.ima)
            plt.title("Imagen original")

            plt.subplot(1,3,2)
            plt.imshow(imaT, cmap="gray")
            plt.title("Imagen sin dibujo")

            ima_cir = cv2.circle(imaT, (X,Y), 200, (255,255,255), -4)
            cv2.putText(imaT, "Imagen Binarizada", (X1+40,Y1+35), cv2.FONT_ITALIC, 1, (0,0,0), 4, cv2.LINE_AA)
            cv2.putText(imaT, f"Umb: {Umb}", (X1+100,Y), cv2.FONT_ITALIC, 1, (0,0,0), 4, cv2.LINE_AA)
            cv2.putText(imaT, f"Kernel: {kernel}", (X1+70,Y2-15), cv2.FONT_ITALIC, 1, (0,0,0), 4, cv2.LINE_AA)

            plt.subplot(1,3,3)
            plt.imshow(ima_cir)
            plt.title("Imagen con dibujo")

            plt.savefig(f"{clave} binarizada.png")
            plt.show()
            
        else:
            print("Valor no válido")




    