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

def fig_prob_n_clientes_en_cola(total_time_custm_in_q):
    customers = []
    for i in range(len(total_time_custm_in_q)):
        customers.append(i)
    count=0
    index = 0
    for cli in total_time_custm_in_q:
        if cli == 0:
            count = count + 1
        if count ==10:
            break
        index = index + 1
    total_time_custm_in_q = total_time_custm_in_q[:index]
    customers= customers[:index]
    ######################
    plt.bar(customers, total_time_custm_in_q)
    plt.title('Probabilidad de encontrar n clientes en cola')
    plt.xlabel('Cant. Clientes')
    plt.ylabel('P(n)')
    plt.show()

def grafico_probabilidad_denegacion_servicio(lista):
    n = ['0', '2', '5', '10', '50', '70', '90', '100']
    plt.bar(n, lista)
    plt.title('Probabilidad de Denegación de Servicio')
    plt.ylim(0,1.2)
    plt.xlabel('Longitud Max. de la Cola')
    plt.ylabel('Probabilidad')
    plt.show()

def grafico_funcionporpartes_valoresdiscretos(intervalos):
    x_points = []
    y_points = []
    valores=[]
    for start, end, q in intervalos:
        x_points.extend([start, end])
        y_points.extend([q,q])
        valores.append(q)
    fig, ax = plt.subplots()
    ax.plot(x_points, y_points, label='Cantidad de clientes en cola')
    ax.set_yticks(valores)
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Cantidad de Clientes')
    ax.set_title('Q(t)')
    ax.legend()
    plt.show()

def probabilidad_denegacion_servicio(quantity_arrived_for_time_unit, quantity_delayed_for_time_unit ):
#Para colas de tamaño [0, 2, 5, 10, 50]
    rho = quantity_arrived_for_time_unit/quantity_delayed_for_time_unit
    n = [0, 2, 5, 10, 50,70, 90, 100]
    service_denegation_probability = []
    for K in n:
        if rho == 1:
            p0 = 1 / (K + 1)
        else:
            p0 = (1 - rho) / (1 - pow(rho,(K + 1)))
        service_denegation_probability.append(p0 * pow(rho,K))
        print(f'K={K} - p0={p0} - rho={rho} - Prob: {p0 * (rho**K)} ')
    return service_denegation_probability


def grafico_server_status(utilizaciones):
    x_points = []
    y_points = []
    valores=[0,1]
    for start, end, server_status in utilizaciones:
        x_points.extend([start, end])
        y_points.extend([server_status,server_status])
    fig, ax = plt.subplots()
    ax.step(x_points, y_points, where='post', label='f(x)', color='b', linewidth=1)
    ax.set_yticks(valores)
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Q(t)')
    ax.set_title('Estatus del servidor a lo largo del tiempo')
    ax.legend()
    plt.show()

#### funcion para calcular el promedio en cola. 
def total_time_in_queue_of_clients(total_time_custm_in_q_array:list[list]):
    max_len = max(len(sublist) for sublist in total_time_custm_in_q_array)
    for sublist in total_time_custm_in_q_array:
        if len(sublist) < max_len:
            while len(sublist) < max_len:
                sublist.append(0)
    poblational_list = [0]*max_len
    for i in range(max_len):
        for sublist in total_time_custm_in_q_array:
            poblational_list[i] += sublist[i]
    for i in range(max_len):
        poblational_list[i] /= len(total_time_custm_in_q_array)
    
    return poblational_list

###


def multiple_runings_program(interarrival = 1, service= 0.5):
    global mean_interarrival
    global mean_service

    mean_interarrival = interarrival #lambda - 1(min)
    mean_service = service #mu - 0.5(min)
    quantity_delayed_for_time_unit_array = []
    quantity_arrived_for_time_unit_array = []
    avg_delay_queue_array = []
    avg_custm_queue_array = []
    server_utilization_array = []
    avg_time_in_system_array = []
    avg_custm_in_system_array = []
    total_time_custm_in_q_array = []
    sim_time_array=[]
    run = 0
    total_of_runnings = 1000

    while run <= total_of_runnings:
        run += 1
        QUEUE_INFTY = False
        if QUEUE_INFTY:
            Q_LIMIT = 100000^99
        else:
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
        """
        global mean_interarrival
        global mean_service
        mean_service = 0.500 #mu - (min)
        mean_interarrival = mean_service*1.750  # 1.000 #lambda - (min)
        """
        sim_time = 0.0 #Clock - Simulation Time
        total_time_custm_in_q = [0.0] * (Q_LIMIT + 1) #en la pos n se acumulan las veces que hubo n clientes en cola
        total_of_delays = 0.0
        total_of_arrivals = 0 #creo que es inutil esto
        #Main
        first_costumer = exponencial(mean_interarrival)
        event_list = [first_costumer, pow(2,30)] 
        time_last_event = 0
        time_arrival = []
        intervalos = []
        utilizaciones = []
        #while sim_time<=10000:
        while num_custs_delayed < num_delays_requiered:
            #evaluamos tipo de evento
            sim_time, next_event_type = next_event(event_list)
            #calculamos estadisticas
            intervalos.append((time_last_event,sim_time,num_in_q))
            time_since_last_event = sim_time - time_last_event
            time_last_event = sim_time
            area_num_in_q = area_num_in_q + (num_in_q * time_since_last_event)
            total_time_custm_in_q[num_in_q] = total_time_custm_in_q[num_in_q] + time_since_last_event 
            utilizaciones.append((time_last_event,sim_time,server_status))
            area_server_status = area_server_status + (server_status * time_since_last_event)

            if next_event_type==0:
                #arrival
                #programo el proximo evento de arribo
                total_of_arrivals = total_of_arrivals + 1
                event_list[0]=sim_time+exponencial(mean_interarrival)
                if server_status == BUSY:
                    num_in_q = num_in_q + 1
                    if not QUEUE_INFTY:
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
                    total_of_delays = total_of_delays + delay
                    num_custs_delayed = num_custs_delayed + 1 #aumento uno la cant clientes servidos porque este entrará con el servidor ocupado
                    event_list[1] = sim_time + exponencial(mean_service)
                    time_arrival = time_arrival[1:] #elimino de la cola el que tomo servicio    

        quantity_delayed_for_time_unit = total_of_delays/sim_time #mu
        quantity_arrived_for_time_unit = total_of_arrivals/sim_time #landa
        avg_delay_queue = (total_of_delays/num_custs_delayed) #tiempo promedio en cola
        avg_custm_queue = (area_num_in_q/sim_time) #q(n)
        server_utilization = (area_server_status/sim_time)*100
        avg_time_in_system = avg_delay_queue + 1/quantity_delayed_for_time_unit #ACA HAY UN ERROR
        avg_service_time = 1 / (server_utilization/100)
        #avg_time_in_system = avg_service_time + avg_delay_queue
        #avg_custm_in_system = quantity_arrived_for_time_unit * avg_time_in_system
        avg_custm_in_system = avg_custm_queue + server_utilization/100

        total_time_custm_in_q = [round((cli/sim_time)*100,3) for cli in total_time_custm_in_q] #p_index

        quantity_delayed_for_time_unit_array.append(quantity_delayed_for_time_unit)
        quantity_arrived_for_time_unit_array.append(quantity_arrived_for_time_unit)
        avg_delay_queue_array.append(avg_delay_queue)
        avg_custm_queue_array.append(avg_custm_queue)
        server_utilization_array.append(server_utilization)
        avg_time_in_system_array.append(avg_time_in_system)
        avg_custm_in_system_array.append(avg_custm_in_system)
        total_time_custm_in_q_array.append(total_time_custm_in_q)
        sim_time_array.append(sim_time)

        """
        print('-----------------------------------------------------------')
        print(f'Mean Interarrival time:                 {mean_interarrival} min.')
        print(f'Mean Service Time:                      {mean_service} min.')
        print(f'Number of customers:                    {num_delays_requiered}')  
        print()
        print(f'Promedio de clientes en el sistema:     {round(avg_custm_in_system,3)} clientes')
        print(f'Promedio de clientes en cola q(n):      {round(avg_custm_queue,3)} clientes')
        print(f'Tiempo promedio en el sistema:          {round(avg_time_in_system,3)} min.')
        print(f'Promedio de espera en cola:             {round(avg_delay_queue,3)} min.')
        print(f'Utilizacion del servidor:               {round(server_utilization,3)}%')
        print(f'Tiempo de Simulación:                   {round(sim_time,3)} min.')
        print()
        print()


        fig_prob_n_clientes_en_cola(total_time_custm_in_q)
        #grafico_funcionporpartes_valoresdiscretos(intervalos)
        #grafico_server_status(utilizaciones)
        #service_denegation_probability = probabilidad_denegacion_servicio(quantity_arrived_for_time_unit, quantity_delayed_for_time_unit )
        #grafico_probabilidad_denegacion_servicio(service_denegation_probability)
        """


    quantity_delayed_for_time_unit = sum(quantity_delayed_for_time_unit_array)/len(quantity_delayed_for_time_unit_array)
    quantity_arrived_for_time_unit = sum(quantity_arrived_for_time_unit_array)/len(quantity_arrived_for_time_unit_array)
    avg_delay_queue = sum(avg_delay_queue_array)/len(avg_delay_queue_array)
    avg_custm_queue = sum(avg_custm_queue_array)/len(avg_custm_queue_array)
    server_utilization = sum(server_utilization_array)/len(server_utilization_array)
    avg_time_in_system = sum(avg_time_in_system_array) / len(avg_time_in_system_array)
    avg_custm_in_system = sum(avg_custm_in_system_array)/ len(avg_custm_in_system_array)
    sim_time = sum(sim_time_array)/len(sim_time_array)



    total_time_custm_in_q = total_time_in_queue_of_clients(total_time_custm_in_q_array)


    print('-----------------------------------------------------------')
    print(f'Mean Interarrival time:                 {mean_interarrival} min.')
    print(f'Mean Service Time:                      {mean_service} min.')
    print(f'Number of customers:                    {num_delays_requiered}')
    print(f'Number of runnings:                     {total_of_runnings}')  
    print()
    print(f'Promedio de clientes en el sistema:     {round(avg_custm_in_system,3)} clientes')
    print(f'Promedio de clientes en cola q(n):      {round(avg_custm_queue,3)} clientes')
    print(f'Tiempo promedio en el sistema:          {round(avg_time_in_system,3)} min.')
    print(f'Promedio de espera en cola:             {round(avg_delay_queue,3)} min.')
    print(f'Utilizacion del servidor:               {round(server_utilization,3)}%')
    print(f'Tiempo de Simulación:                   {round(sim_time,3)} min.')
    print()
    print()

    fig_prob_n_clientes_en_cola(total_time_custm_in_q)

