import random
from graphics import relative_frequency, cash_evolution
#Metodo D'Alembert
def dalembert_strategy(number_of_players, initial_bet, n, initial_capital= float('inf')):
    i=1
    x=1
    winning_attemptAcc = []
    cash_evolutionPlayers = []
    bet = initial_bet
    if initial_capital == float('inf'):
        print('Metodo DAlembert: capital Infinito')
    else:
        print('Metodo DAlembert: capital Finito')
        print(initial_capital)
    for x in range(1, number_of_players + 1):
        i=1
        winning_attempt = []
        cash_flow = []
        if initial_capital == float('inf'):
            cash_flow.append(0)
        else:
            cash_flow.append(initial_capital)

        while i<=n and (cash_flow[-1] >= 0 or initial_capital == float('inf')):
            wagered = 'p' #PAR
            parity = 'i'
            attempt = 1
            while parity != wagered and i<=n and (cash_flow[-1] >= 0 or initial_capital == float('inf')):
                i += 1 #Acumulo un giro de ruleta
                result = random.randint(0, 36) 
                if result == 0 :
                    parity = 'n'
                elif result % 2 == 0 :
                    parity = 'p'
                else: parity = 'i'
                #evaluo si gano
                if parity != wagered : #Perdida
                    cash_flow.append(cash_flow[-1] - bet) 
                    bet += 1
                    attempt += 1
                else: 
                    winning_attempt.append(attempt)  #Guardamos attempt ganadora
                    cash_flow.append(cash_flow[-1] + bet) 
                    if bet > 1:
                        bet -= 1
        print('Flujo de caja:', cash_flow )
        print('Tirada ganadora:', winning_attempt)
        winning_attemptAcc.append(winning_attempt)
        cash_evolutionPlayers.append(cash_flow)
    relative_frequency(winning_attemptAcc)
    cash_evolution(cash_evolutionPlayers)