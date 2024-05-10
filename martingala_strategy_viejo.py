import random
from graphics import cash_evolution, GRAF_FREC_RELATIVA, GRAF_VARCAP
## Infinito
#METODO MARTINGALA
def martingala_strategy(n, apuestaInicial, capitalInicial):
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
            valorGanador = random.randint(0, 36) 
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


## Finito marcos
def martingala_strategy_finito(number_of_players, initial_bet, initial_capital, rounds):
    cash_evolution_players = []
    for j in range(0, number_of_players):
        cash_in_hand = initial_capital
        bet = initial_bet
        cash_evolution = [cash_in_hand]

        for i in range(0, rounds):

            result = random.randint(0, 37)
            
            if cash_in_hand>0:

                if (result % 2 == 0) & (result!=0):
                    cash_in_hand = cash_in_hand + bet
                    bet = initial_bet
                else:
                    cash_in_hand = cash_in_hand - bet
                    bet = 2*bet
                    if bet>cash_in_hand:
                        bet = cash_in_hand

            cash_evolution.append(cash_in_hand)
        
        cash_evolution_players.append(cash_evolution)

    cash_evolution(cash_evolution_players)

martingala_strategy(number_of_players, initial_bet, initial_capital, n)