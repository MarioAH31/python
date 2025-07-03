import os
from textwrap import indent
import time

def menu():
    #borrado de pantalla
    os.system("cls")
    print("1. Ingresar un nuevo aprendiz")
    print("2. Ingresar el ID del aprendiz")
    print("3. Promedio aprendiz")
    print("4. Promedio area")
    print("5. Promedio General")
    print("6. Mostrar aprendices")
    print("7. Salir")

def validarId(identificacion):
    identi = int(input(f"Ingrese una ID: {identificacion}"))
    while(0 > identi or identi > 99):
        print("Identificación invalida, debe estar entre 0 y 99")
        identi = int(input(f"Ingrese una ID: {identificacion}"))
    return identi 
    

def validarNota(competencia):
    nota = float(input(f"Ingrese la nota de {competencia}: "))
    while (0>nota or nota>5):
        print("Nota invalida, debe estar entre 0 y 5")
        nota = float(input(f"Ingrese la nota de {competencia}: "))
    return nota


def ingresarAprendiz():
    nombre = input("Ingrese el nombre del aprendiz: ")
    id = input("Identificación: ")

    notaAlgoritmos = validarNota("Algoritmos")
    notaAnalisis = validarNota("Análisis")
    notaFisica = validarNota("Física")

    #agregar aprendiz a la lista
    aprendices.append(nombre)
    notasAlgoritmos.append(notaAlgoritmos)
    notasAnalisis.append(notaAnalisis)
    notasFisica.append(notaFisica)
    
    print()
    print("Aprendiz agregado correctamente")
    time.sleep(1)

def mostrarAprendices():
    cantidad = len(aprendices)      
    if cantidad == 0:
        print("No hay aprendices registrados")
    else:
        i = 0
        while i < cantidad:
            print("Nombre: ",aprendices[i])
            print("Algoritmos: ",notasAlgoritmos[i])
            print("Analisis: ",notasAnalisis[i])
            print("Fisica: ",notasFisica[i])
            print()
            i += 1
   

# BLOQUE PRINCIPAL
aprendices = []
notasAlgoritmos = []
notasAnalisis = []
notasFisica = []
id = []
opcion = 0

while opcion != 6:
    menu()
    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        case 1:
            print("Ingresar un nuevo alumno")
            ingresarAprendiz()
        case 2:
            print("ID del aprendiz")
            input()
        case 3:
            print("Promedio aprendiz")
            input()
        case 4:
            print("Promedio area")
            input()
        case 5:
            print("Promedio General")
            input()
        case 6:
            mostrarAprendices()
            input("presione ENTER para continuar")
        case 7:
            print("Salir")
            time.sleep(1)            

        case _:
            print("Opcion no valida")
            input()

print("Fin del programa")