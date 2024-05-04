import random
from graphics import GRAF_FREC_RELATIVA, GRAF_VARCAP
#Metodo D'Alembert
def dalembert_strategy(n, apuestaInicial):
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
            valorGanador = random.randint(0, 36) 
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