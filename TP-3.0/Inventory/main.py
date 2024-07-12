import numpy as np
import random
import matplotlib.pyplot as plt

# Integer variables
amount = 0 
max_inventory = 0
initial_inv_level = 0
inv_level = 0
next_event_type = 0
num_events = 0
num_months = 0
num_values_demand = 0
min_inventory = 0
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
#costos finales con todas las corridas
final_tot = 0.0
final_holding = 0.0
final_shortage = 0.0
final_ordering = 0.0
# Lists
prob_distrib_demand = []
#costos por cada corrida
total_costs = []
ordering_costs = []
holding_costs = []
shortage_costs = []
#costos por politica o mes
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
    global inv_level, amount, total_ordering_cost, time_next_event, sim_time, min_inventory, max_inventory, setup_cost, incremental_cost, minlag, maxlag
    global area_holding, area_shortage, num_months, holding_cost, shortage_cost
    if inv_level < min_inventory: 
        amount = max_inventory - inv_level
        total_ordering_cost += setup_cost + amount * incremental_cost
        
        time_next_event[1] = sim_time + uniform(minlag, maxlag)


    # Calcula y devuelve estimaciones de medidas deseadas de rendimiento.
    avg_holding_cost = holding_cost * area_holding / num_months
    avg_shortage_cost = shortage_cost * area_shortage / num_months
    avg_ordering_cost = total_ordering_cost / num_months
    
    tot_per_pol.append(avg_holding_cost + avg_shortage_cost + avg_ordering_cost)
    ord_per_pol.append(avg_ordering_cost)
    hold_per_pol.append(avg_holding_cost)
    short_per_pol.append(avg_shortage_cost)
    time_next_event[4] = sim_time + 1.0 # Programa el evento de evaluación

def report():
    global area_holding, area_shortage, total_ordering_cost, num_months, min_inventory, max_inventory, holding_cost, shortage_cost
    global final_tot, final_holding, final_shortage, final_ordering
    global total_costs, ordering_costs, holding_costs, shortage_costs
    global tot_per_pol, ord_per_pol, hold_per_pol, short_per_pol
    # Calcula y devuelve estimaciones de medidas deseadas de rendimiento.
    avg_holding_cost = holding_cost * area_holding / num_months
    avg_shortage_cost = shortage_cost * area_shortage / num_months
    avg_ordering_cost = total_ordering_cost / num_months
    # Suma el acumulado total
    final_tot += avg_holding_cost + avg_shortage_cost + avg_ordering_cost
    final_holding += avg_holding_cost
    final_shortage += avg_shortage_cost
    final_ordering += avg_ordering_cost

    total_costs.append(avg_holding_cost + avg_shortage_cost + avg_ordering_cost)
    ordering_costs.append(avg_ordering_cost)
    holding_costs.append(avg_holding_cost)
    shortage_costs.append(avg_shortage_cost)
    print("\n\n{:<15}{:<15}{:<15}{:<15}{:<15}".format(
        "Min/Max Inv", "Total Cost", "Order Cost", "Hold Cost", "Short Cost"))
    print("\n\n({}, {}){:>15.2f}{:>15.2f}{:>15.2f}{:>15.2f}".format(
        min_inventory, max_inventory, avg_ordering_cost + avg_holding_cost + avg_shortage_cost,
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

def cost_graphs(total_costs, ordering_costs, holding_costs, shortage_costs, min_inventories, max_inventories):
    
    policies = []

    for small, big in zip(min_inventories, max_inventories):
        policy = f"Policy: {small}-{big}"
        policies.append(policy)
        policies = [...]

    # Configuración de la gráfica de barras
    x = range(len(policies))
    width = 0.2              # Ancho de las barras

    # Creación de la figura y los ejes
    fig, ax = plt.subplots()

    # Creación de las barras para cada tipo de costo
    bar1 = ax.bar(x, total_costs, width, label='Total Cost')
    bar2 = ax.bar([i + width for i in x], ordering_costs, width, label='Ordering Cost')
    bar3 = ax.bar([i + 2*width for i in x], holding_costs, width, label='Holding Cost')
    bar4 = ax.bar([i + 3*width for i in x], shortage_costs, width, label='Shortage Cost')

    # Etiquetas de los ejes y título de la gráfica
    ax.set_xlabel('Tipo de costo')
    ax.set_ylabel('Valor')
    ax.set_title('Costos finales')
    ax.set_xticks([i + 1.5*width for i in x])
    ax.set_xticklabels(policies)

    # Leyenda de la gráfica
    ax.legend()
    # Mostrar la gráfica
    plt.show()

def cost_pie_chart(ordering_costs, holding_costs, shortage_costs, min_inventories, max_inventories):
    
    policies = []

    for small, big in zip(min_inventories, max_inventories):
        policy = f"Policy: {small}-{big}"
        policies.append(policy)
        policies = [...]

    # Creación de la figura y los ejes
    fig, ax = plt.subplots()

    # Creación del gráfico de torta
    labels = ['Ordering Cost', 'Holding Cost', 'Shortage Cost']
    sizes = [ordering_costs, holding_costs, shortage_costs]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

    # Título de la gráfica
    ax.set_title('Costos finales')

    # Mostrar la gráfica
    plt.show()

def cost_per_policy_graphs(tot_per_pol, ord_per_pol, hold_per_pol, short_per_pol, min_inventories, max_inventories):
    """
    Crea una gráfica de barras que muestra el desglose de costos por políticas de inventario.
    :param tot_per_pol: Lista de costos totales por política.
    :param ord_per_pol: Lista de costos de pedido por política.
    :param hold_per_pol: Lista de costos de mantenimiento por política.
    :param short_per_pol: Lista de costos de escasez por política.
    :param min_inventories: Lista de valores 'small' para cada política.
    :param max_inventories: Lista de valores 'big' para cada política.
    """
  
    # Crear etiquetas de políticas
    policies = [f"Policy: {small}-{big}" for small, big in zip(min_inventories, max_inventories)]

    # Configuración de la gráfica de barras
    x = np.arange(len(policies))
    width = 0.2  # Ancho de las barras

    # Creación de la figura y los ejes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Creación de las barras para cada tipo de costo
    bar1 = ax.bar(x - 1.5*width, tot_per_pol, width, label='Total Cost', color='b')
    bar2 = ax.bar(x - 0.5*width, ord_per_pol, width, label='Ordering Cost', color='g')
    bar3 = ax.bar(x + 0.5*width, hold_per_pol, width, label='Holding Cost', color='r')
    bar4 = ax.bar(x + 1.5*width, short_per_pol, width, label='Shortage Cost', color='c')

    # Etiquetas de los ejes y título de la gráfica
    ax.set_xlabel('Políticas de Inventario', fontsize=12)
    ax.set_ylabel('Valor', fontsize=12)
    ax.set_title('Desglose de Costos por Política de Inventario', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(policies, rotation=45, ha='right')

    # Leyenda de la gráfica
    ax.legend()

    # Ajuste de diseño
    fig.tight_layout()

    # Mostrar la gráfica
    plt.show()

def time_cost_graphs(months, total_costs, ordering_costs, holding_costs, shortage_costs):
    """
    Crea una gráfica de líneas que muestra la variación de costos a lo largo del tiempo.

    :param months: Número de meses.
    :param total_costs: Lista de costos totales por mes.
    :param ordering_costs: Lista de costos de pedido por mes.
    :param holding_costs: Lista de costos de mantenimiento por mes.
    :param shortage_costs: Lista de costos de escasez por mes.
    """
    
    # Crear el rango de meses
    x = np.arange(1, months + 1)

    # Configuración de la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x, total_costs, marker='o', linestyle='-', label='Total Costs', color='b')
    plt.plot(x, ordering_costs, marker='s', linestyle='--', label='Ordering Costs', color='g')
    plt.plot(x, holding_costs, marker='^', linestyle='--', label='Holding Costs', color='r')
    plt.plot(x, shortage_costs, marker='d', linestyle='--', label='Shortage Costs', color='c')

    # Etiquetas de los ejes y título de la gráfica
    plt.xlabel('Meses', fontsize=12)
    plt.ylabel('Valor', fontsize=12)
    plt.title('Variación de Costos a lo Largo del Tiempo', fontsize=14)

    # Leyenda de la gráfica
    plt.legend()

    # Ajuste de diseño
    plt.tight_layout()

    # Mostrar la gráfica
    plt.show()


def main():
    global k, prob_distrib_demand, num_events, num_policies, min_inventory, max_inventory, num_months, num_values_demand, mean_interdemand, setup_cost, incremental_cost, holding_cost, shortage_cost, minlag, maxlag, min_inventories, max_inventories
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

    # Parámetros de "min_inventory" y "max_inventory" del libro
    num_events = 4
    k = 0
    min_inventories = [20, 20, 20, 20, 40, 40, 40, 60, 60]
    max_inventories = [40, 60, 80, 100, 60, 80, 100, 80, 100]



    prob_distrib_demand = [0.0] * (int(num_values_demand) + 1)
    # for i in range(1, int(num_values_demand) + 1):
    #     prob_distrib_demand[i] = float(input("Ingrese el valor de prob_distrib_demand en {}: ".format(i))) # Se ingresan las probabilidades de que la demanda sea de i unidades
    prob_distrib_demand[1] = 0.16666666666666666
    prob_distrib_demand[2] = 0.3333333333333333
    prob_distrib_demand[3] = 0.3333333333333333
    prob_distrib_demand[4] = 0.16666666666666666
    # Corre la simulación variando la política de inventario

    for i in range(1, int(num_policies) + 1):

        # Lee la política de inventario e inicializa la simulación
        min_inventory = min_inventories[k]
        max_inventory = max_inventories[k]
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
        k += 1
    
    print("\n\n" + "\033[4m" + "Final costs" + "\033[0m")
    print("Total cost:", round(final_tot, 2))
    print("Ordering cost:", round(final_ordering, 2))
    print("Holding cost:", round(final_holding, 2))
    print("Shortage cost:", round(final_shortage, 2))
    cost_graphs(final_tot, final_ordering, final_holding, final_shortage, min_inventories, max_inventories)
    cost_pie_chart(final_ordering, final_holding, final_shortage, min_inventories, max_inventories)
    cost_per_policy_graphs(tot_per_pol, ord_per_pol, hold_per_pol, short_per_pol, min_inventories, max_inventories)  
    time_cost_graphs(num_months,tot_per_pol, ord_per_pol, hold_per_pol, short_per_pol)    
main()
