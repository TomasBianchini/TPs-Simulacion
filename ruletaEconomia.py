import random 
import matplotlib.pyplot as plt
import sys 
import numpy as np

def tirarRuleta():
    return random.randint(0, 36) 



#METODO MARTINGALA
def MET_MARTINGALA(n, apuestaInicial, capitalInicial):
    print('Metodo Martingala')
    # n = 10 lo comente porque lo pase a funcion
    i=0
    tiradaGanadora = []
    flujoCaja = []
    # apuestaInicial = 5 lo comente porque lo pase a funcion
    #capitalInicial = 5
    flujoCaja.append(0)
    flujoApuestas = []
    flujoApuestas.append(0)
    while i <= n:
        apuesta = apuestaInicial
        perdido = 0
        apostado = 'p' #PAR
        paridad = 'i'
        tirada = 1
        while paridad != apostado: # and i!=n: (lo comente porque me queda en bucle infinito)
            i += 1 #acumulo un giro de ruleta
            valorGanador = tirarRuleta()
            flujoCaja.append(flujoCaja[-1] - apuesta) 
            flujoApuestas.append(-apuesta)
            if valorGanador == 0 :
                paridad = 'n'
            elif valorGanador % 2 == 0 :
                paridad = 'p'
            else: paridad = 'i'
            #evaluo si gano
            if paridad != apostado :
                perdido += apuesta
            #flujoCaja.append(flujoCaja[-1] - apuesta) #lo perdi. 
                apuesta *= 2
            #flujoCaja.append(flujoCaja[-1] - apuesta) #guardo lo que vuelvo a apostar. 
                tirada += 1
            else: 
                tiradaGanadora.append(tirada)  #Guardamos tirada ganaroda
                flujoCaja.append(flujoCaja[-1] + 2*apuesta)
                flujoApuestas.append(2*apuesta)

    #print('Ganaste en la: ', tirada)
    #print('Ganaste: $', apuesta - perdido)
    #print('Flujo Apuestas: ', flujoApuestas)
    print('Flujo de caja:', flujoCaja )
    print('Tirada ganadora:', tiradaGanadora)
    GRAF_FREC_RELATIVA(tiradaGanadora)
    GRAF_VARCAP(flujoCaja)


#Metodo D'Alembert
def MET_DALEMBERT(n, apuestaInicial):
    print('Metodo DAlembert')
    i=1
    tiradaGanadora = []
    flujoCaja = []
    apuesta = apuestaInicial
    flujoCaja.append(0)
    flujoApuestas = []
    flujoApuestas.append(0)

    while i<=n:
        apostado = 'p' #PAR
        paridad = 'i'
        tirada = 1
        while paridad != apostado and i<=n:
            i += 1 #acumulo un giro de ruleta
            valorGanador = tirarRuleta()
            if valorGanador == 0 :
                paridad = 'n'
            elif valorGanador % 2 == 0 :
                paridad = 'p'
            else: paridad = 'i'
            #evaluo si gano
            if paridad != apostado : #Perdida
                flujoCaja.append(flujoCaja[-1] - apuesta) 
                apuesta += 1
                tirada += 1
            else: 
                tiradaGanadora.append(tirada)  #Guardamos tirada ganadora
                flujoCaja.append(flujoCaja[-1] + apuesta) 
                if apuesta > 1:
                    apuesta -= 1
    print('Flujo de caja:', flujoCaja )
    print('Tirada ganadora:', tiradaGanadora)
    GRAF_FREC_RELATIVA(tiradaGanadora)
    GRAF_VARCAP(flujoCaja)


#Grafico de Fracuencia Relativa
def GRAF_FREC_RELATIVA(tiradaGanadora):
    frecuencia_numeros = {}
    for numero in tiradaGanadora:
        if numero in frecuencia_numeros:
            frecuencia_numeros[numero] += 1
        else:
            frecuencia_numeros[numero] = 1
    frecuencia_relativa = {numero: frecuencia / len(tiradaGanadora) for numero, frecuencia in frecuencia_numeros.items()}
    frecuencia_relativa_ordenada = {numero: frecuencia_relativa[numero] for numero in sorted(frecuencia_relativa.keys())}
    plt.bar(frecuencia_relativa_ordenada.keys(), frecuencia_relativa_ordenada.values())
    plt.xlabel('Número')
    plt.ylabel('Frecuencia Relativa')
    plt.title('Frecuencia Relativa de Números en tiradaGanadora')
    plt.show()

#Grafico de variacion de capital
def GRAF_VARCAP(flujoCaja):
    plt.figure("Flujo de caja con respecto a N")
    plt.title("Flujo de caja con respecto a N")
    plt.xlabel("N (numero de tiradas")
    plt.ylabel("CC (cantidad de capital)")
    plt.axhline(y=0, color='b')
    plt.plot(range(1, len(flujoCaja) + 1), flujoCaja)
    plt.grid(True)
    plt.show()


MET_MARTINGALA(100,5,5)
MET_DALEMBERT(100,5)