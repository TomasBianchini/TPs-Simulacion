import random

def tirarRuleta():
    return random.randint(0, 36) 

#METODO MARTINGALA
apuestaInicial = 5
perdido = 0
apostado = 'p'
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

print('Ganaste en la: ', tirada)
print('Ganaste: $', apuestaInicial - perdido)



