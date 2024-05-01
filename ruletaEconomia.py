import random

def tirarRuleta():
    return random.randint(0, 36) 



#METODO MARTINGALA
n = 10
i=0
tiradaGanadora = []
flujoCaja = []
apuestaInicial = 5
flujoCaja.append(0)
while i <= n:
    apuesta = apuestaInicial
    perdido = 0
    apostado = 'p' #PAR
    paridad = 'i'
    tirada = 1
    while paridad != apostado :
        i += 1 #acumulo un giro de ruleta
        valorGanador = tirarRuleta()
        if valorGanador == 0 :
            paridad = 'n'
        elif valorGanador % 2 == 0 :
            paridad = 'p'
        else: paridad = 'i'
        #evaluo si gano
        if paridad != apostado :
            perdido += apuesta
            flujoCaja.append(-apuesta) #lo perdi. 
            apuesta *= 2
            tirada += 1
        else: 
            tiradaGanadora.append(tirada)  #Guardamos tirada ganaroda
            flujoCaja.append(apuesta)

print('Ganaste en la: ', tirada)
print('Ganaste: $', apuesta - perdido)




