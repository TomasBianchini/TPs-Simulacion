import random

def tirarRuleta():
    return random.randint(0, 36) 



#METODO MARTINGALA
n = 10
tiradaGanadora = []
for i in range (1,n):
    apuestaInicial = 5
    perdido = 0
    apostado = 'p' #PAR
    paridad = 'i'
    tirada = 1
    while paridad != apostado :
        valorGanador = tirarRuleta()
        if valorGanador == 0 :
            paridad = 'n'
        elif valorGanador % 2 == 0 :
            paridad = 'p'
        else: paridad = 'i'
        #evaluo si gano
        if paridad != apostado :
            perdido += apuestaInicial
            apuestaInicial *= 2
            tirada += 1
        else: 
            tiradaGanadora.append(tirada)  #Guardamos tirada ganaroda

print('Ganaste en la: ', tirada)
print('Ganaste: $', apuestaInicial - perdido)



