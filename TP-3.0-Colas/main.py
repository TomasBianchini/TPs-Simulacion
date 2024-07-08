import random
import math
from utilities import *

def exponencial(beta):
    U = random.random()
    return round((-beta * math.log(U)),2)

BUSY = 1 #Ocupado
IDLE = 0  #Inactivo
Q_LIMIT = 100 #Limite de la cola
n = 1000 #Cantidad de demoras completadas (condición de fin)

#VARIABLES

media_interarribo = 1.0
media_servicio = 0.5

#SistemState
server_status = IDLE
number_in_queue = 0
time_of_arraival=[]
arrivals=[]
departures=[]
time_of_last_event=0
#General
clock = 0
event_list=[] #0->Arrival 1->Delayed
event_list.append(0)
event_list.append(0)
#Statistical Counters
number_delayed = 0
total_delay=0
area_under_q=0
area_under_d=0

times_interarrival=[]
times_services=[]

event_list[1]=1000000

def time_generator():
    times_interarrival=[]
    times_services=[]
    for i in range(1,n+1):
        times_interarrival.append(exponencial(media_interarribo))
        times_services.append(exponencial(media_servicio))
    return times_interarrival, times_services

    """
    arrivals.append(times_interarrival[0])
    departures.append(round((times_services[0]+times_interarrival[0]),2))
    for i in range(0,n-1):
        arrivals.append(round((times_interarrival[i+1]+arrivals[i]),2))
        departures.append(round((departures[i]+times_services[i+1]),2))

    print("Tiempos de interarribo:", times_interarrival)
    print("Tiempos de servicio:", times_services)
    print("Tiempos de arrivo:", arrivals)
    print("Tiempos de salida:", departures)
    """


####### MAIN ################


times_interarrival, times_services = time_generator()

event_list[0] = times_interarrival[0]
#times_arrival.append(tiempo_entre_llegadas)
clock+= event_list[0]
server_status = BUSY
event_list[1]= times_services[0]

while number_delayed < n:
    print()



    if number_in_queue >= Q_LIMIT:
        raise ValueError("Error, la cola se ha llenado.") #Alerta. 
        break 








""" tiempo_entre_llegadas = exponencial(media_interarribo)
print(f"Tiempo entre llegadas: {tiempo_entre_llegadas}")

tiempo_servicio = exponencial(media_servicio)
print(f"Tiempo de servicio: {tiempo_servicio}") """

"""
    t=0 --> 
        iniciar las variables. ejecutar un tiempo entre llegadas. 
        Programar el evento de llegada. Chequeo el estatus del servidor
            OCUPADO: (No, estara siempre desocupado)
            LIBRE: Demora para el cliente uno = 0. Ejecutar tiempo de servicio.
                    Modifico el estado a ocupado. Sumo 1 a la cantidad de demoras. Programo el evento
                    de salida. Recopilo los datos necesarios. 
"""

 