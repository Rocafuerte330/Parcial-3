#NOMBRES - Grupo - Informática 2
#Jose David Román Restrepo  - Grupo 2
#Santiago Heredia Vasquez  - Grupo 4
#GitHub: https://github.com/Rocafuerte330/Parcial-3
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pydicom
import os
from Clases import *
ruta = "archivosDCM"

def menu():
    while True:
        try:
            opcion = int(input("""Seleccione una opción:
1. Cargar archivos Dicom y recosntruir volumen
2. Mostrar cortes
3. Aplicar traslación                          
4. Ingresar imagen (JPG o PNG)
5. Binarización de imagen (JPG o PNG)
6. Salir
R// """))
            return opcion
        except ValueError:
            print(" Entrada inválida. Por favor ingrese un número.")
            continue

def main():
    archivos_DICOM_IMA = {}
    paciente = {}
    while True:
        R = menu()

        if R == 1:
            print(" Cargando archivos DICOM...")
            archivos = cargar_carpeta_dicom(ruta)
            volumen = reconstruir_volumen(archivos)
            paciente = crear_paciente(archivos, volumen)
            print(f" Paciente cargado: {paciente.nombre}, Edad: {paciente.edad}, ID: {paciente.ID}")
            print(f" Volumen reconstruido con forma: {paciente.imagen.shape}")

        elif R == 2:
            if paciente is None:
                print(" Primero debe cargar los archivos DICOM (opción 1).")
            else:
                mostrar_cortes(paciente.imagen)

        elif R == 3:
            if paciente is None:
                print("Primero debe cargar los archivos DICOM (opción 1).")
            else:
                aplicar_traslacion_corte_transversal(paciente.imagen)
        elif R == 4:
            imagenes = os.listdir("Imagenes")
            print("""Estas son las imagenes disponibles, escriba el nombre de la imagen.
NOTA: Incluya la extención de la imagen (.jpg o .png)
Ejemplo: imagen.png""")
            for i in imagenes:
                print(f"- {i}")
            Ruta_ima = input("R// ")

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
            clave = input("R// ")
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
            ima_bin =im.binarizar_imagen(binarizacion, kernel, dibujo, clave)      

        elif R == 6:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")
if __name__ == "__main__":
    main()