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


######## VAMOS DEVUELTA! #############
import matplotlib.pyplot as plt
import numpy as np

def funcionporpartes_sinconfigurareje():

    # Definir los puntos de los intervalos y los valores de la función en esos intervalos
    intervalos = [(0, 2.6), (2.6, 3.8), (3.8, 4)]
    valores = [1, 2, 1]

    # Crear las listas de puntos x e y
    x_points = []
    y_points = []

    # Agregar los puntos de los intervalos a las listas
    for i, (start, end) in enumerate(intervalos):
        x_points.extend([start, end])
        y_points.extend([valores[i], valores[i]])

    # Crear la figura y el eje
    fig, ax = plt.subplots()

    # Dibujar la línea continua
    ax.plot(x_points, y_points, label='f(x) definida por tramos')

    # Añadir etiquetas y título
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Función definida por tramos')
    ax.legend()

    # Mostrar la gráfica
    plt.show()


############# GRAFICO 2 CON VALORES DISCRETOS #################### 
def grafico_funcionporpartes_valoresdiscretos(intervalos, valores):

    # Definir los puntos de los intervalos y los valores de la función en esos intervalos
    intervalos = [(0, 2.6), (2.6, 3.8), (3.8, 4)]
    valores = [1, 2, 1]

    # Crear las listas de puntos x e y
    x_points = []
    y_points = []

    # Agregar los puntos de los intervalos a las listas
    for i, (start, end) in enumerate(intervalos):
        x_points.extend([start, end])
        y_points.extend([valores[i], valores[i]])

    # Crear la figura y el eje
    fig, ax = plt.subplots()

    # Dibujar la línea continua
    ax.plot(x_points, y_points, label='f(x) definida por tramos')

    # Configurar los ticks del eje y para mostrar solo valores discretos
    ax.set_yticks(valores)

    # Añadir etiquetas y título
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Función definida por tramos')
    ax.legend()

    # Mostrar la gráfica
    plt.show()
