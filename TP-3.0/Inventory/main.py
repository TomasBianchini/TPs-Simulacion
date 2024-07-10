import numpy as np
import random

# Integer variables
amount = 0 
bigs = 0
initial_inv_level = 0
inv_level = 0
next_event_type = 0
num_events = 0
num_months = 0
num_values_demand = 0
smalls = 0
# Float variables
area_holding = 0.0
area_shortage = 0.0
holding_cost = 0.0
incremental_cost = 0.0
maxlag = 0.0
mean_interdemand = 0.0
minlag = 0.0
setup_cost = 0.0
shortage_cost = 0.0
sim_time = 0.0
time_last_event = 0.0
time_next_event = [0.0] * 5
total_ordering_cost = 0.0
final_tot = 0.0
final_holding = 0.0
final_shortage = 0.0
final_ordering = 0.0
# Lists
prob_distrib_demand = []
total_costs = []
ordering_costs = []
holding_costs = []
shortage_costs = []
tot_per_pol = []
ord_per_pol = []
hold_per_pol = []
short_per_pol = []


def expon(mean):
    return np.random.exponential(mean)

def uniform(a, b):
    # Función de generación de una variable uniforme. Devuelve una variable aleatoria U(a, b)
    return np.random.uniform(a, b)

def random_integer(prob_distrib):
    valores = [0,1,2,3,4]
    return random.choices(valores, prob_distrib)[0]


def timing():
    global sim_time, next_event_type, time_next_event, num_events
    # Determina el siguiente tipo de evento y avanza el reloj de simulación
    min_time_next_event = 1.0e+30
    next_event_type = 0

    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i

    # if next_event_type == 0:
    #     print("Event list empty at time {}".format(sim_time))
    #     exit(1)
    sim_time = min_time_next_event


def initailize():
    global sim_time, inv_level, time_last_event, total_ordering_cost, area_holding, area_shortage, time_next_event
    global final_tot, final_holding, final_shortage, final_ordering, num_months
    # Inicializa el reloj de simulación
    sim_time = 0.0

    # Inicializa las variables de estado
    inv_level = initial_inv_level
    time_last_event = 0.0

    # Inicializa los contadores estadísticos
    total_ordering_cost = 0.0
    area_holding = 0.0
    area_shortage = 0.0

    # Inicializa la lista de eventos. Como no hay pedidos pendientes, el evento de llegada 
    # del pedido se elimina de la consideración
    time_next_event[1] = 1.0e+30 #Tiempo grande porque no hay pedidos pendientes
    time_next_event[2] = sim_time + expon(mean_interdemand)
    time_next_event[3] = num_months
    time_next_event[4] = 0.0

def orden_arrival(): 
    global inv_level, time_next_event
    inv_level += amount
    time_next_event[1] = 1.0e+30 #Tiempo grande porque ya recibio el pedido

def demand():
    global inv_level, time_next_event
    inv_level -= random_integer(prob_distrib_demand)

    # Programa la hora de la siguiente demanda
    time_next_event[2] = sim_time + expon(mean_interdemand)

def evaluate():
    global inv_level, amount, total_ordering_cost, time_next_event, sim_time, smalls, bigs, setup_cost, incremental_cost, minlag, maxlag
    if inv_level < smalls: 
        amount = bigs - inv_level
        total_ordering_cost += setup_cost + amount * incremental_cost
        
        time_next_event[1] = sim_time + uniform(minlag, maxlag)

    time_next_event[4] = sim_time + 1.0 # Programa el evento de evaluación

def report():
    global area_holding, area_shortage, total_ordering_cost, num_months, smalls, bigs, holding_cost, shortage_cost
    global final_tot, final_holding, final_shortage, final_ordering
    global total_costs, ordering_costs, holding_costs, shortage_costs
    global tot_per_pol, ord_per_pol, hold_per_pol, short_per_pol
    # Calcula y devuelve estimaciones de medidas deseadas de rendimiento.
    avg_holding_cost = holding_cost * area_holding / num_months
    avg_shortage_cost = shortage_cost * area_shortage / num_months
    avg_ordering_cost = total_ordering_cost / num_months
    # # Suma el acumulado total
    # final_tot += avg_holding_cost + avg_shortage_cost + avg_ordering_cost
    # final_holding += avg_holding_cost
    # final_shortage += avg_shortage_cost
    # final_ordering += avg_ordering_cost

    # tot_per_pol.append(avg_holding_cost + avg_shortage_cost + avg_ordering_cost)
    # ord_per_pol.append(avg_ordering_cost)
    # hold_per_pol.append(avg_holding_cost)
    # short_per_pol.append(avg_shortage_cost)

    # total_costs.append(avg_holding_cost + avg_shortage_cost + avg_ordering_cost)
    # ordering_costs.append(avg_ordering_cost)
    # holding_costs.append(avg_holding_cost)
    # shortage_costs.append(avg_shortage_cost)

    print("\n\n({}, {}){:>15.2f}{:>15.2f}{:>15.2f}{:>15.2f}".format(
        smalls, bigs, avg_ordering_cost + avg_holding_cost + avg_shortage_cost,
        avg_ordering_cost, avg_holding_cost, avg_shortage_cost))


def update_time_avg_status():
    global sim_time, time_last_event, inv_level, area_shortage, area_holding
    # Calcula el tiempo desde el último evento y actualiza el tiempo del último evento
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    # Determina el estado del nivel del inventario durante el intervalo anterior
    # Si el nivel del inventario durante el intervalo anterior era negativo, se actualiza area_shortage
    # Si era positivo, se actualiza area_holding
    # Si era cero no se actualiza nada
    if inv_level < 0:
        area_shortage -= inv_level * time_since_last_event
    elif inv_level > 0:
        area_holding += inv_level * time_since_last_event

def main():
    global k, prob_distrib_demand, num_events, num_policies, smalls, bigs, num_months, num_values_demand, mean_interdemand, setup_cost, incremental_cost, holding_cost, shortage_cost, minlag, maxlag
    global total_costs, ordering_costs, holding_costs, shortage_costs
    # Ingreso de los parámetros de entrada
    # initial_inv_level = float(input("Ingrese el valor de initial_inv_level: "))
    # num_months = float(input("Ingrese el valor de num_months: "))
    # num_policies = float(input("Ingrese el valor de num_policies: "))
    # num_values_demand = float(input("Ingrese el valor de num_values_demand: "))
    # mean_interdemand = float(input("Ingrese el valor de mean_interdemand: "))
    # setup_cost = float(input("Ingrese el valor de setup_cost: "))
    # incremental_cost = float(input("Ingrese el valor de incremental_cost: "))
    # holding_cost = float(input("Ingrese el valor de holding_cost: "))
    # shortage_cost = float(input("Ingrese el valor de shortage_cost: "))
    # minlag = float(input("Ingrese el valor de minlag: "))
    # maxlag = float(input("Ingrese el valor de maxlag: "))

    # Valores de ejemplo del libro:
    initial_inv_level, num_months, num_policies, num_values_demand, mean_interdemand, setup_cost, incremental_cost, holding_cost, shortage_cost, minlag, maxlag = 60, 9, 9, 4, 0.10, 32, 3, 1, 5, 0.5, 1

    print(num_months)

    # Parámetros de "smalls" y "bigs" del libro
    smalls = 20
    bigs = 40    
    num_events = 4


    prob_distrib_demand = [0.0] * (int(num_values_demand) + 1)
    for i in range(1, int(num_values_demand) + 1):
        prob_distrib_demand[i] = float(input("Ingrese el valor de prob_distrib_demand en {}: ".format(i))) # Se ingresan las probabilidades de que la demanda sea de i unidades

    initailize()

    while(next_event_type != 3):
        timing()
        update_time_avg_status()
        if(next_event_type == 1):
            orden_arrival()
        elif(next_event_type == 2):           
            demand()
        elif(next_event_type == 4):
            evaluate()
        else:
            report()
    
    print("\n\n" + "\033[4m" + "Final costs" + "\033[0m")
    print("Total cost:", round(final_tot, 2))
    print("Ordering cost:", round(final_ordering, 2))
    print("Holding cost:", round(final_holding, 2))
    print("Shortage cost:", round(final_shortage, 2))


main()