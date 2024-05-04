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
def MET_LABOUCHERE(n, apuestaInicial, capital=float('inf')):
    print('Metodo Labouchere')
    i = 1
    tiradaGanadora = []
    flujoCaja = []
    apuestas = apuestaInicial.copy()  # Copiar la lista de apuestas iniciales
    flujoCaja.append(0)
    apuestas_iniciales = apuestaInicial.copy()  # Mantener una copia de la lista de apuestas iniciales
    
    while i <= n:
        
        apostado = 'p' # Apostar a la paridad par
        paridad = 'i'  # Empezar asumiendo una paridad diferente a la apostada
        tirada = 1
        
        
        while paridad != apostado and i <= n:
            apuesta = apuestas[0] if len(apuestas) == 1 else apuestas[0] + apuestas[-1] 
            i += 1  # Acumular un giro de ruleta
            valorGanador = tirarRuleta()  # Supongamos que hay una función tirarRuleta() que devuelve el valor ganador
            if valorGanador == 0:
                paridad = 'n'  # Si el valor ganador es 0, se considera como "nulo"
            elif valorGanador % 2 == 0:
                paridad = 'p'  # Si el valor ganador es par, la paridad es 'p'
            else:
                paridad = 'i'  # Si el valor ganador es impar, la paridad es 'i'
            
            # Evaluar si se ganó o se perdió
            if paridad != apostado:  # Pérdida
                flujoCaja.append(flujoCaja[-1] - apuesta)
                if len(apuestas) > 1:
                    apuestas.append(apuesta)  # Agregar la suma de la primera y última apuesta a la lista
                tirada += 1
            else:  # Ganancia
                tiradaGanadora.append(tirada)  # Guardar tirada ganadora
                flujoCaja.append(flujoCaja[-1] + apuesta)
                if len(apuestas) > 1:
                    apuestas.pop(0)  # Eliminar la primera apuesta
                    apuestas.pop(-1)  # Eliminar la última apuesta
            if not apuestas:  # Si la lista de apuestas está vacía, restaurarla a su estado original
                apuestas = apuestas_iniciales.copy()
            if (apuestas[0] + apuestas[-1] > capital) or capital + flujoCaja[-1] < 0 or -flujoCaja[-1]+(apuestas[0] + apuestas[-1]) > capital:
                print('Capital:', capital, 'Flujo de caja:', flujoCaja[-1], 'Apuesta futura:', (apuestas[0] + apuestas[-1]),'apuestas',apuestas)
                break  # Salir del bucle si el capital se agota o se alcanza el límite
        
        if(apuestas[0] + apuestas[-1] > capital) or capital + flujoCaja[-1] < 0 or -flujoCaja[-1]+(apuestas[0] + apuestas[-1]) > capital:
            print("Se alcanzó el límite de capital negativo. Salir del método.")
            break
    
    print('Flujo de caja:', flujoCaja)
    print('Tirada ganadora:', tiradaGanadora)
    GRAF_FREC_RELATIVA(tiradaGanadora)
    GRAF_VARCAP(flujoCaja)
#MET_MARTINGALA(100,5,5)
#MET_DALEMBERT(100,5)
MET_LABOUCHERE(100, [1, 2, 3, 4, 5],10)




        #METODO Fibonacci
def fibonacci(capitalInicial =float('inf')):
    n = 10
    i=0
    tiradaGanadora = []
    flujoCaja = []
    apuestaInicial = 5
    flujoCaja.append(0 if capitalInicial == float('inf') else capitalInicial)
    flujoApuestas = []
    flujoApuestas.append(0)
    while i <= n:
        apuesta = apuestaInicial
        perdido = 0
        apostado = 'p' #PAR
        paridad = 'i'
        tirada = 1
        while (paridad != apostado and i <=n and (perdido + apuesta) <= capitalInicial):
            i += 1 #acumulo un giro de ruleta
            valorGanador = tirarRuleta()
            flujoCaja.append(flujoCaja[-1] - apuesta) 
            flujoApuestas.append(apuesta)
            if valorGanador == 0 :
                paridad = 'n'
            elif valorGanador % 2 == 0 :
                paridad = 'p'
            else: paridad = 'i'
            #evaluo si gano
            if paridad != apostado:
                perdido += apuesta
                if(tirada == 1):
                    apuesta = apuestaInicial
                else:
                    apuesta = flujoApuestas[-2] + flujoApuestas[-1]
                tirada += 1
            # if(perdido + apuesta > capitalInicial):
            #     break
            else: 
                tiradaGanadora.append(tirada)  #Guardamos tirada ganadora
                flujoCaja.append(flujoCaja[-1] + 2*apuesta)
        if perdido + apuesta > capitalInicial:
            break
    print('Flujo Apuestas: ', flujoApuestas)
    print('Flujo de caja:', flujoCaja )
    print('Tirada ganadora:', tiradaGanadora)
    
fibonacci()