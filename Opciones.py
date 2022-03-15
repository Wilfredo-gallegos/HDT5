#Wilfredo Gallegs
#Hoja de trabajo 5

import Simulador as simulador
import simpy
import random

def variables(instrucciones_recibidos,intervalo_recibidos, procesos_recibidos):
    simulador.procesos=procesos_recibidos
    simulador.intervalo=intervalo_recibidos
    simulador.instrucciones=instrucciones_recibidos

def tiempo_promedio():
    tiempo_promedio=simulador.tiempo_total/simulador.procesos
