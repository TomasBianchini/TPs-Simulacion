from graphics import cash_evolution, GRAF_VARCAP
import random

#METODO Fibonacci
def fibonacci_strategy(number_of_players, initial_bet, n ,initial_capital = float('inf')):
    print('Metodo Fibonacci')

    cash_evolution_players = []
    for j in range(0,number_of_players):
        i=0
        tiradaGanadora = []
        cash_evolution = []
        cash_evolution.append(0 if initial_capital == float('inf') else initial_capital)
        bet_evolution = []
        while i <= n+1 and (cash_evolution[-1] > 0 or initial_capital == float('inf') ):
            bet = initial_bet
            lost = 0
            apostado = 'p' #PAR
            paridad = 'i'
            tirada = 1
            while (paridad != apostado and i <=n+1 and (bet <= cash_evolution[-1] or initial_capital == float('inf'))):
                i += 1 
                result = random.randint(0, 36) 
                cash_evolution.append(cash_evolution[-1] - bet) 
                bet_evolution.append(bet)
                if result == 0 :
                    paridad = 'n'
                elif result % 2 == 0 :
                    paridad = 'p'
                else: paridad = 'i'
                #evaluo si gano
                if paridad != apostado:
                    lost += bet
                    if(tirada == 1):
                        bet = initial_bet
                    else:
                        bet = bet_evolution[-2] + bet_evolution[-1]
                    tirada += 1
                else: 
                    tiradaGanadora.append(tirada)  
                    cash_evolution.append(cash_evolution[-1] + 2*bet)
        cash_evolution_players.append(cash_evolution)
        GRAF_VARCAP(cash_evolution)
    cash_evolution, GRAF_FREC_RELATIVA, GRAF_VARCAP(cash_evolution_players)