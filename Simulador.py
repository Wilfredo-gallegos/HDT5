#Wilfredo Gallegs
#Hoja de trabajo 5

import simpy
import random
env = simpy.Environment()
procesos = 0
intervalo=0.0
instrucciones=0
tiempo_actual=0.0
tiempos = []
tiempo_total=0.0

RAM = simpy.Container(env, init=100, capacity=100)

y para tomar memoria del RAM: RAM.get(memoria)
y para devolver memoria al RAM: RAM.put(memoria)

def variables(instrucciones_recibidos,intervalo_recibidos, procesos_recibidos):
    procesos=procesos_recibidos
    intervalo=intervalo_recibidos
    instrucciones=instrucciones_recibidos

def simulacion(env,instrucciones,intervalo,procesos):
    yield env.timeout(tiempo_actual)
    print(" ")

    for i in range(procesos):
        tiempo = random.expovariate(1.0 / intervalo)
        ram_usada = random.uniform(1, 10)
        env.procces(simulacion(env, instrucciones, intervalo, procesos))
env.run()