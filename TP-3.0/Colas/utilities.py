import random
import math

def exponencial(beta):
    U = random.random()
    return round((-beta * math.log(U)),2)


def time_generator(media_interarribo, media_servicio):
    times_interarrival=[]
    times_services=[]
    for i in range(1,n+1):
        times_interarrival.append(exponencial(media_interarribo))
        times_services.append(exponencial(media_servicio))
    return times_interarrival, times_services

def is_queue_full(Q_LIMIT, number_in_queue):
    if number_in_queue >= Q_LIMIT:
        raise ValueError("Error, la cola se ha llenado.") #Alerta. 
        return True
    else:
        return False
