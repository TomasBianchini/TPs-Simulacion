import random
import math
import matplotlib.pyplot as plt

def exponencial(beta):
    U = random.random()
    return round((-beta * math.log(U)),2)

def next_event(event_list: list):
    if event_list[0]< event_list[1]:
        return event_list[0], 0 #arrive 
    else:
        return event_list[1], 1 #departure


Q_LIMIT = 100
BUSY = 1
IDLE = 0

next_event_type = 0
num_custs_delayed = 0
num_delays_requiered = 1000
num_in_q = 0   #Q(t) -no cuenta el cliente en servicio-
server_status = IDLE

area_num_in_q = 0.0
area_server_status = 0.0
mean_interarrival = 1.0
mean_service = 0.5
sim_time = 0.0 #Clock - Simulation Time
#time_arrival = [0.0] * (Q_LIMIT + 1)

total_of_delays = 0.0




#### Medidas a calcular
# promedio de clientes en cola = area under q(t)
# promedio de clientes en el sistema = 
# tiempo promedio en sistema = 
# tiempo promedio en cola = 
# utilizacion del servidor
# probabilidad de encontrar n clientes en cola = 
# probabilidad de denegacion de servicio = 
####



#Main
first_costumer = exponencial(mean_interarrival)
event_list = [first_costumer, pow(2,30)] #Obligamos al primer evento a ser una llegada
# event_list[0]: ARRIVE --- # event_list[1]: DEPART
time_last_event = 0
time_arrival = []
while num_custs_delayed < num_delays_requiered:
    print(f'Servidos: {num_custs_delayed} - En Cola: {num_in_q}')
    #evaluamos tipo de evento
    sim_time, next_event_type = next_event(event_list)
    print (f'Proximo Evento: {next_event_type} - Simulación Tiempo: {sim_time}')
    #calculamos estadisticas
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    area_num_in_q = num_in_q * time_since_last_event
    area_server_status = server_status * time_since_last_event

    if next_event_type==0:
        #arrival
        #programo el proximo evento de arribo
        event_list[0]=sim_time+exponencial(mean_interarrival)
        if server_status == BUSY:
            num_in_q = num_in_q + 1
            if num_in_q > Q_LIMIT:
                raise ValueError(f'LA COLA SE HA LLENADO - Tiempo: {sim_time} - Clientes servidos: {num_custs_delayed}')
            time_arrival.append(sim_time) #agrego a la cola esta llegada
        else:
            delay = 0
            total_of_delays = total_of_delays + delay
            num_custs_delayed = num_custs_delayed + 1
            server_status = BUSY
            event_list[1]=sim_time+exponencial(mean_service)

    else: 
        #departur
        if num_in_q == 0:
            server_status = IDLE
            event_list[1]=pow(2,30)
        else:
            num_in_q = num_in_q - 1
            delay = sim_time - time_arrival[0]
            num_custs_delayed = num_custs_delayed + 1 #aumento uno la cant clientes servidos porque este entrará con el servidor ocupado
            event_list[1] = sim_time + exponencial(mean_service)
            time_arrival = time_arrival[1:] #elimino de la cola el que tomo servicio    

avg_delay_queue = total_of_delays/num_custs_delayed
avg_custm_queue = area_num_in_q/sim_time
server_utilization = area_server_status/sim_time
print(f'Promedio de espera en cola: {avg_delay_queue}')
print(f'Promedio de clientes en cola: {avg_custm_queue}')
print(f'Utilizacion del servidor: {server_utilization}%')































































"""
while num_in_q<Q_LIMIT:

    if event_list[0] <= event_list[1]:
        #Seteamos el tiempo de la simulacion al momento del evento
        sim_time = event_list[0]
        #Implica que el proximo evento es un arribo
        if server_status == IDLE:
            #El servidor esta libre entonces el cliente entra automaticamente a servicio. 
            #genero el evento de salida
            event_list[1]=sim_time + exponencial(mean_service)
            times_departures.append(event_list[1])
            tuplas_eventos.append((event_list[1], 'D'))
            num_custs_delayed +=1
            delay=0 #el cliente tiene 0 tiempo de espera
            total_of_delays += delay
            #cambio el estado del servidor
            server_status = BUSY
        else: #El servidor estaba ocupado
            num_in_q +=1
        print()
        #genero un proximo evento de llegada
        event_list[0] = sim_time + exponencial(mean_interarrival)
        times_arrivals.append(event_list[0])
        tuplas_eventos.append((event_list[0], 'A'))
        
    else:
        
        #El proximo evento es una salida
        #Seteamos el tiempo de la simulacion al momento del evento
        sim_time = event_list[1]
        print()



"""

