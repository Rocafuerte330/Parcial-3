
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pydicom
import os
from Clases import *

def menu():
    return int(input("""Seleccione una opción:
1. Procesar archivos Dicom
2. Ingresar paciente
3. Transformación Geométrica de un Dicom
4. Imgresar imagen (JPG o PNG)
5. Binarización de imagen (JPG o PNG)
6. Salir
R// """))
def main():
    archivos_DICOM_IMA = {}
    pacientes = {}
    while True:
        R = menu()

        if R == 1:
            pass
        elif R == 2:
            pass
        elif R == 3:
            pass
        elif R == 4:
            imagenes = os.listdir("Imagenes")
            print("""Estas son las imagenes disponibles, escriba el nombre de la imagen.
NOTA: Incluya la extención de la imagen (.jpg o .png)
Ejemplo: imagen.png""")
            for i in imagenes:
                print(f"- {i}")
            # Ruta_ima = input("R// ")
            Ruta_ima = "rostro.jpg"

            ima = IMAGENES(Ruta_ima,None)
            ima.cargar_imagen()
            # ima.mostrar_imagen()
            clave = os.path.splitext(Ruta_ima)[0]
            print(clave)
            archivos_DICOM_IMA[clave] = ima
            print(archivos_DICOM_IMA)

        elif R == 5:
            print("""Escoja la imagen a binarizar""")
            imagenes = list(archivos_DICOM_IMA.keys())
            for i in imagenes:
                print(f"- {i}")
            # clave = input("R// ")
            clave = "rostro"
            Ruta = f"{clave}.jpg"
            ima = archivos_DICOM_IMA.get(clave,"No está en el diccionario")
            img = ima.ima
            im = IMAGENES(None, img)
            print("""Escoja el tipo de binarización que desea realizar:
1. Binario → cv2.THRESH_BINARY
2. Binario invertido → cv2.THRESH_BINARY_INV
3. Truncado → cv2.THRESH_TRUNC
4. Tozero → cv2.THRESH_TOZERO
5. Tozero invertido → cv2.THRESH_TOZERO_INV""")
            binarizacion = int(input("R// "))
            print("Ingrese el tamaño del kernel:")
            row = int(input("Filas: "))
            col = int(input("Columnas: "))
            kernel = (row,col)
            dibujo = int(input("""Escoja un dibujo:
1. Cuadrado
2. Circulo
R// """))
            ima_bin =im.binarizar_imagen(binarizacion, kernel, dibujo, Ruta)      
            archivos_DICOM_IMA[f"{clave} binarizada"] = ima_bin

        elif R == 6:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")
if __name__ == "__main__":
    main()