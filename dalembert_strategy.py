import random
from graphics import GRAF_FREC_RELATIVA, GRAF_VARCAP
#Metodo D'Alembert
def dalembert_strategy(number_of_players, initial_bet, n, initial_capital):
    i=1
    Winning_AttemptAcc = []
    Cash_EvolutionPlayers = []
    bet = initial_bet
    if initial_capital == 'i':
        print('Metodo DAlembert: capital Infinito')
    else:
        print('Metodo DAlembert: capital Finito')
        print(initial_capital)
    for i in range(1, number_of_players + 1):
        Winning_Attempt = []
        Cash_Evolution = []
        if initial_capital == 'i':
            Cash_Evolution.append(0)
        else:
            Cash_Evolution.append(initial_capital)

        while i<=n and (Cash_Evolution[-1] >= 0 or initial_capital == 'i'):
            wagered = 'p' #PAR
            parity = 'i'
            Attempt = 1
            while parity != wagered and i<=n and (Cash_Evolution[-1] >= 0 or initial_capital == 'i'):
                i += 1 #Acumulo un giro de ruleta
                result = random.randint(0, 36) 
                if result == 0 :
                    parity = 'n'
                elif result % 2 == 0 :
                    parity = 'p'
                else: parity = 'i'
                #evaluo si gano
                if parity != wagered : #Perdida
                    Cash_Evolution.append(Cash_Evolution[-1] - bet) 
                    bet += 1
                    Attempt += 1
                else: 
                    Winning_Attempt.append(Attempt)  #Guardamos Attempt ganadora
                    Cash_Evolution.append(Cash_Evolution[-1] + bet) 
                    if bet > 1:
                        bet -= 1
        print('Flujo de caja:', Cash_Evolution )
        print('Tirada ganadora:', Winning_Attempt)
        Winning_AttemptAcc.append(Winning_Attempt)
        Cash_EvolutionPlayers.append(Cash_Evolution)
    GRAF_FREC_RELATIVA(Winning_AttemptAcc)
    GRAF_VARCAP(Cash_EvolutionPlayers, initial_capital)