#Wilfredo Gallegs
#Hoja de trabajo 5

import Simulador as simulador
import Opciones as opciones
Stay=True
while Stay == True:
    print("\n Simulacion de corridas de programas de un sistema operativo")
    print("Que desea hacer?")
    print("1) Ver tiempo promedio")
    print("2) ver desviacion estandar del tiempo")
    print("3) salir")
    opcion = input()
    try:
        opcion = int(opcion)
        if opcion == 1:
            print("opcion 1")
            procesos=int(input("Cual es la cantidad de procesos a llevar a cabo?"))
            intervalo = int(input("Cual es el intervalo del proceso a llevar a cabo?"))
            instrucciones = int(input("Cual es la cantidad de instrucciones procesos a llevar a cabo?"))
            opciones.variables(instrucciones,intervalo,procesos)
        elif opcion == 2:
            print("opcion 1")
            Stay = False
        else:
            print("no dentro del rango")
    except:
        print("valor no es un numero")