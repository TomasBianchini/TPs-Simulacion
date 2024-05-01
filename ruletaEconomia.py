import random

def tirarRuleta():
    return random.randint(0, 36) 



#METODO MARTINGALA
n = 10
i=0
tiradaGanadora = []
flujoCaja = []
apuestaInicial = 5
capitalInicial = 5
flujoCaja.append(0)
flujoApuestas = []
flujoApuestas.append(0)
while i <= n:
    apuesta = apuestaInicial
    perdido = 0
    apostado = 'p' #PAR
    paridad = 'i'
    tirada = 1
    while paridad != apostado and i!=n:
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

print('Ganaste en la: ', tirada)
print('Ganaste: $', apuesta - perdido)
print('Flujo Apuestas: ', flujoApuestas)
print('Flujo de caja:', flujoCaja )
print('Tirada ganadora:', tiradaGanadora)



