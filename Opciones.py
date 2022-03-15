#Wilfredo Gallegs
#Hoja de trabajo 5

import Simulador as simulador
import simpy
import random

tiempo_promedio=0.0
def variables(instrucciones_recibidos,intervalo_recibidos, procesos_recibidos):
    simulador.procesos=procesos_recibidos
    simulador.intervalo=intervalo_recibidos
    simulador.instrucciones=instrucciones_recibidos

def tiempo_promedio():
    tiempo_promedio=(simulador.tiempo_total/simulador.procesos)
    print("El tiempo promedio es: ",tiempo_promedio)