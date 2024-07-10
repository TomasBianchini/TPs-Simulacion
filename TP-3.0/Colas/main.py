import random
import math
from utilities import *



BUSY = 1 #Ocupado
IDLE = 0  #Inactivo
Q_LIMIT = 100 #Limite de la cola
n = 5 #Cantidad de demoras completadas (condición de fin)

#VARIABLES

media_interarribo = 1.0
media_servicio = 0.5



#vent_list=[]       #0->Arrival 1->Delayed
#Statistical Counters

i_arrival=0 
i_service=0

times_interarrival=[]
times_services=[]




def arrival(server_status,number_in_queue,number_delayed):
    if server_status == BUSY:
        number_in_queue+=1
        if is_queue_full(Q_LIMIT, number_in_queue):
            print('Pase el value error') 
    else:
        server_status = BUSY
        number_delayed +=1
    return server_status, number_in_queue, number_delayed 



def delayed(number_in_queue, server_status,event_list):
    if number_in_queue == 0:
        server_status = IDLE
        event_list[1] = 1000000000000
    else:
        number_in_queue -= 1
        server_status=BUSY
    return server_status, event_list, number_in_queue



def next_event(event_list, times_interarrival, times_services, i_arrival, i_service):
    if event_list[0] <= event_list[1]:
        next = 'A'
        clock = event_list[0]
        event_list[0] += times_interarrival[i_arrival]
        i_arrival += 1 
    else:
        next ='D'
        clock = event_list[1]
        event_list[1] += times_services[i_service]
        i_service += 1
    return   i_arrival, i_service, clock, next

####### MAIN ################


#times_interarrival, times_services = time_generator(media_interarribo, media_servicio)
times_interarrival = [0.4, 1.2, 0.5, 1.7, 0.2, 1.6, 0.2, 1.4]
times_services = [2.0, 0.7, 0.2, 1.1, 3.7 ]

event_list = [times_interarrival[i_arrival], 1000000000000]
i_arrival += 1 
clock = 0
server_status = IDLE
number_in_queue = 0
time_of_arrival=[]
time_of_last_event=0
number_delayed = 0
total_delay=0
area_under_q=0
area_under_d=0
i=0
print(f'Corrida {i} - Event List: {event_list}')
while number_delayed < n:
    i+=1
    i_arrival, i_service, clock, next = next_event(event_list, times_interarrival, times_services, i_arrival, i_service)
    print(f'Corrida {i} - Event List: {event_list}')
    if next == 'A':
        server_status, number_in_queue, number_delayed = arrival(server_status,number_in_queue,number_delayed)
    else: 
        server_status, event_list, number_in_queue = delayed(number_in_queue,server_status)









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

 