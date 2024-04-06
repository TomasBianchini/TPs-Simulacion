import random 
import matplotlib.pyplot as plt
import sys 


def GRAF_FRECUENCIA(frecuencia_relativa):
    plt.figure("Frecuencia relativa de x con respecto a n")
    plt.title("Frecuencia relativa de x con respecto a n")
    plt.xlabel("Numero de tiradas")
    plt.ylabel("fr (frecuencia relativa)")
    plt.axhline(y=1/37, color='b')
    plt.plot(frecuencia_relativa, 'r-')
    plt.show()


prom = 18
#TODO pasarlo a argumentos de entrada  
if len(sys.argv) != 7 or sys.argv[1] != "-t" or sys.argv[3] != "-c" or sys.argv[5] != "-n":
    print("Uso: python programa.py -t <num_tiradas> -c <num_corridas> -n <num>")
    sys.exit(1)
corridas = []

cant_tiradas = int(sys.argv[2])
cant_corridas = int(sys.argv[4])
numero = int(sys.argv[6])
frecuencia_relativa_corridas = []
for j in range (0,cant_corridas):
    frecuencia_absoluta = {}
    frecuencia_relativa = []
    valores = []
    # valores = [random.randint(0, 36) for _ in range(cant_tiradas)]
    for i in range(cant_tiradas): 
        valores.append(random.randint(0, 36))
        frecuencia_relativa.append(valores.count(numero) / (i + 1))
    print(frecuencia_relativa)
    print(valores)
    GRAF_FRECUENCIA(frecuencia_relativa)


    for i in range(0,37):
        frecuencia_absoluta[i] = valores.count(i)
        # frecuencia_relativa[i] =  frecuencia_absoluta[i] / cant_tiradas
    # print("Valores generados:", valores)
    # for i in range(0, 37):
        # print("Frecuencia absoluta de ", i, ":", frecuencia_absoluta[i])
        # print("Frecuencia relativa de ", i, ":", frecuencia_relativa[i])
    corridas.append(frecuencia_absoluta)