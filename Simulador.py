#Wilfredo Gallegs
#Hoja de trabajo 5

import simpy
import random
import psutil


env = simpy.Environment()
CPU = simpy.Resource (env, capacity=2)
esperar = simpy.Resource (env, capacity=2)
procesos = 50
intervalo=10
instrucciones=6
tiempo_actual=0.0
tiempos = []
tiempo_total=0.0
instrucciones_completas=0
RAM = simpy.Container(env, init=100, capacity=100)

#y para tomar memoria del RAM: RAM.get(memoria)
#y para devolver memoria al RAM: RAM.put(memoria)

def variables(instrucciones_recibidos,intervalo_recibidos, procesos_recibidos):
    procesos=procesos_recibidos
    intervalo=intervalo_recibidos
    instrucciones=instrucciones_recibidos

def simulacion(i,env,instrucciones,intervalo,procesos,tiempo,ramusada,RAM,tiempo_total1,instrucciones_completas):
    yield env.timeout(tiempo)
    print(i,". utiliza ",ramusada,"de ram")
    tiempo_entrada = env.now
    yield RAM.get(ram_usada)

    while instrucciones_completas < instrucciones:
        yield CPU.request()
        yield env.timeout(instrucciones_completas/instrucciones)

        instrucciones_completas =instrucciones_completas+1
        yield env.timeout(1)
    tiempo_total1=tiempo_total1+env.now+tiempo_entrada+ramusada
    tiempos.append(env.now)


for i in range(procesos):
    tiempo = random.expovariate(1.0 / intervalo)
    ram_usada = random.uniform(1, 10)

    env.process(simulacion(i,env, instrucciones, intervalo, procesos,tiempo, ram_usada,RAM,tiempo_total,instrucciones_completas))




env.run()
