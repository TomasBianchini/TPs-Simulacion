import random 
import matplotlib.pyplot as plt
import sys 
import numpy as np

colores = ['r', 'g', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']

def GRAF_DESVIO(desvio_corridas):
    plt.figure("Valor del desvio del numero X con respecto a n")
    plt.title("Valor del desvio del numero X con respecto a n")
    plt.xlabel("Numero de tiradas")
    plt.ylabel("vd (valor del desvio)")
    plt.axhline(10.67, color='b')
    for i, desvio in enumerate(desvio_corridas):
        color = colores[i % len(colores)]  
        plt.plot(desvio, color=color)
    plt.show()

def GRAF_VARIANZA(varianza_corridas):
    plt.figure("Valor del varianza del numero X con respecto a n")
    plt.title("Valor del varianza del numero X con respecto a n")
    plt.xlabel("Numero de tiradas")
    plt.ylabel("vv (valor de la varianza)")
    plt.axhline(114, color='b')
    for i, varianza in enumerate(varianza_corridas):
        color = colores[i % len(colores)]  
        plt.plot(varianza, color=color)
    plt.show()

def GRAF_PROMEDIO(promedio_corridas):
    plt.figure("Promedio de las tiradas con respecto a n")
    plt.title("Promedio de las tiradas con respecto a n")
    plt.xlabel("Numero de tiradas")
    plt.ylabel("vp (valor promedio)")
    plt.axhline(18, color='b')
    for i, promedio in enumerate(promedio_corridas):
        color = colores[i % len(colores)]  
        plt.plot(promedio, color=color)
    plt.show()

def GRAF_FRECUENCIA(frecuencia_relativa_corridas):
    plt.figure("Frecuencia relativa de x con respecto a n")
    plt.title("Frecuencia relativa de x con respecto a n")
    plt.xlabel("Numero de tiradas")
    plt.ylabel("fr (frecuencia relativa)")
    plt.axhline(y=1/37, color='b')
    for i, frecuencia_relativa in enumerate(frecuencia_relativa_corridas):
        color = colores[i % len(colores)]  
        plt.plot(frecuencia_relativa, color=color)
    plt.show()


if len(sys.argv) != 7 or sys.argv[1] != "-t" or sys.argv[3] != "-c" or sys.argv[5] != "-n":
    print("Uso: python programa.py -t <num_tiradas> -c <num_corridas> -n <num>")
    sys.exit(1)

cant_tiradas = int(sys.argv[2])
cant_corridas = int(sys.argv[4])
numero = int(sys.argv[6])
frecuencia_relativa_corridas = []
promedio_corridas = []
desvio_corridas = []
varianza_corridas = []
for j in range (0,cant_corridas):
    frecuencia_absoluta = {}
    frecuencia_relativa = []
    valores = []
    promedios = []  
    desvio = []
    varianza = []
    for i in range(cant_tiradas): 
        valores.append(random.randint(0, 36))
        frecuencia_relativa.append(valores.count(numero) / (i + 1))
        promedios.append(np.mean(valores))
        desvio.append(np.std(valores))
        varianza.append(np.var(valores))
        frecuencia_relativa_corridas.append(frecuencia_relativa)
        promedio_corridas.append(promedios)
        desvio_corridas.append(desvio)
        varianza_corridas.append(varianza)
    
GRAF_FRECUENCIA(frecuencia_relativa_corridas)
GRAF_PROMEDIO(promedio_corridas)
GRAF_DESVIO(desvio_corridas)
GRAF_VARIANZA(varianza_corridas)