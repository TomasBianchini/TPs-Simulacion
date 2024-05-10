from graphics import cash_evolution as evolution, GRAF_VARCAP
import random

#METODO Fibonacci
def fibonacci_strategy(number_of_players, initial_bet, n ,initial_capital = float('inf')):
    print('Metodo Fibonacci')

    cash_evolution_players = []
    for j in range(0,number_of_players):
        i=0
        winning_attempt = []
        cash_evolution = []
        cash_evolution.append(0 if initial_capital == float('inf') else initial_capital)
        bet_evolution = []
        while i <= n+1:
            bet = initial_bet
            lost = 0
            wagered  = 'p' #PAR
            parity = 'i'
            attempt = 1
            while (parity != wagered  and i <=n+1):
                i += 1
                result = random.randint(0, 36) 
                if result == 0 :
                    parity = 'n'
                elif result % 2 == 0 :
                    parity = 'p'
                else: parity = 'i'
                ##Evaluamos si tiene
                if(cash_evolution[-1] == 0 and initial_capital != float('inf')):
                    cash_evolution.append(0) 
                elif bet > cash_evolution[-1] and initial_capital != float('inf'):
                    cash_evolution.append(0) 
                    bet_evolution.append(cash_evolution[-1]) 
                    bet = cash_evolution[-1]
                    if parity != wagered :
                        lost += bet
                        #Si pierde termina poruqe no tiene mas plata
                        break
                    else: 
                        #Si gana arranca la secuencia de nuevo
                        winning_attempt.append(attempt)  
                        cash_evolution.append(cash_evolution[-1] + 2*bet)
                        break
                else:
                    cash_evolution.append(cash_evolution[-1] - bet) 
                    bet_evolution.append(bet)
                    #evaluo si gano
                    if parity != wagered :
                        lost += bet
                        if(attempt == 1):
                            bet = initial_bet
                        else:
                            bet = bet_evolution[-2] + bet_evolution[-1]
                        attempt += 1
                    else: 
                        winning_attempt.append(attempt)  
                        cash_evolution.append(cash_evolution[-1] + 2*bet)
        cash_evolution_players.append(cash_evolution)
    evolution(cash_evolution_players)