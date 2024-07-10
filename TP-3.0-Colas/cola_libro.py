import random
import math
import matplotlib.pyplot as plt

def exponencial(beta):
    U = random.random()
    return round((-beta * math.log(U)),2)

Q_LIMIT = 100
BUSY = 1
IDLE = 0

next_event_type = 0
num_custs_delayed = 0
num_delays_requiered = 0
num_events = 0
num_in_q = 0
server_status = IDLE

area_num_in_q = 0.0
area_server_status = 0.0
mean_interarrival = 0.0
mean_service = 0.0
sim_time = 0.0
time_arrival = [0.0] * (Q_LIMIT + 1)
time_last_event = 0.0
time_next_event = [] #event list
total_of_delays = 0.0


def grafics(sim_time_list ):
    plt.figure(figsize=(10, 5))
    plt.hist(arrivals, bins=range(int(max(sim_time_list)) + 2), alpha=0.5, label='Llegadas', edgecolor='black', align='left')
    plt.hist(departures, bins=range(int(max(sim_time_list)) + 2), alpha=0.5, label='Salidas', edgecolor='black', align='left')

    plt.xlabel('Tiempo de Simulación')
    plt.ylabel('Número de Eventos')
    plt.title('Llegadas y Salidas de Clientes a lo Largo del Tiempo de Simulación')
    plt.legend()
    plt.show()


def timing(sim_time,time_next_event,num_events):
    min_time_next_event = 1.0e+29
    next_event_type=0
    for i in range (1,num_events+1,1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event=time_next_event[i]
            next_event_type = i
    #min_time_next_event = min(time_next_event)
    #next_event_type = time_next_event.index(min_time_next_event)
    if next_event_type==0:
        raise ValueError('Event List is Empty')
    sim_time=min_time_next_event
    return sim_time, next_event_type


def arrive(time_next_event, sim_time,server_status,num_in_q,time_arrival,total_of_delays,num_custs_delayed,mean_service,mean_interarrival):
    time_next_event[1]=sim_time+exponencial(mean_interarrival)
    arrivals.append(sim_time)
    if server_status==BUSY:
        num_in_q +=1
        if num_in_q>Q_LIMIT:
            raise ValueError('Cola sobrecargada. Fin de la simulación')
        time_arrival[num_in_q]=sim_time
    else: 
        delay = 0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY
        time_next_event[2]=sim_time+exponencial(mean_service)
    return time_next_event, server_status, num_in_q, time_arrival, total_of_delays, num_custs_delayed

def depart(num_in_q, server_status, time_next_event, sim_time, total_of_delays, num_custs_delayed,time_arrival):
    if num_in_q==0:
        server_status = IDLE
        time_next_event[2]= 1.0e+30
    else:
        num_in_q -=1
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed +=1
        time_next_event[2]=sim_time+exponencial(mean_service)
        #Para mi esta mal copiado 
        for i in range (1, num_in_q+1):
            time_arrival[i] = time_arrival[i+1]
    departures.append(sim_time)  
    return server_status, time_next_event, num_in_q, total_of_delays, num_custs_delayed, time_arrival

def report(total_of_delays, num_custs_delayed, area_num_in_q, sim_time, area_server_status):
    delay_avarege = total_of_delays / num_custs_delayed
    num_q_avarege = area_num_in_q/sim_time
    server_utilization = area_server_status/sim_time
    time_simulation_total = sim_time
    print(f'El tiempo de servicio promedio fue de: {delay_avarege}')
    print(f'La cantidad de clientes promedio fue de: {num_q_avarege}')
    print(f'El servidor fue utilizado en un: {server_utilization}%')
    print(f'La simulacion termino en {time_simulation_total} minutos')

def update_time_avg_status(sim_time, time_last_event, area_num_in_q,area_server_status):
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time 
    area_num_in_q += num_in_q*time_since_last_event
    area_server_status += server_status*time_since_last_event

    return time_last_event, area_num_in_q, area_server_status 

###### MAIN ##########

sim_time_list = []
num_in_q_list = []
global arrivals  
global departures 
arrivals = []
departures = []


mean_interarrival = 1.0
mean_service = 0.5
num_delays_requiered = 1000
num_events = 2

#Inicializamos
time_next_event = [0, sim_time + exponencial(mean_interarrival), 1.0e+30]

while num_custs_delayed < num_delays_requiered:

    print(time_next_event)

    sim_time, next_event_type = timing(sim_time,time_next_event,num_events)

    time_last_event, area_num_in_q, area_server_status = update_time_avg_status(sim_time, time_last_event, area_num_in_q,area_server_status)

    sim_time_list.append(sim_time)
    num_in_q_list.append(num_in_q)

    if next_event_type==1:
        time_next_event, server_status, num_in_q, time_arrival, total_of_delays, num_custs_delayed = arrive(time_next_event, sim_time,server_status,num_in_q,time_arrival,total_of_delays,num_custs_delayed,mean_service,mean_interarrival)
    else: 
        server_status, time_next_event, num_in_q, total_of_delays, num_custs_delayed, time_arrival = depart(num_in_q, server_status, time_next_event, sim_time, total_of_delays, num_custs_delayed,time_arrival)

report(total_of_delays, num_custs_delayed, area_num_in_q, sim_time, area_server_status)

grafics(sim_time_list)
