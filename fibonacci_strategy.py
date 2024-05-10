from graphics import cash_evolution as evolution, relative_frequency
import random

#METODO Fibonacci
def fibonacci_strategy(number_of_players, initial_bet, n ,initial_capital = float('inf')):
    print('Metodo Fibonacci')
    winning_attempts = []
    cash_evolution_players = []
    wagered  = 'p' #PAR
    for j in range(0,number_of_players):
        winning_attempt = []
        cash_evolution = []
        cash_in_hand = initial_capital if initial_capital != float('inf') else 0
        cash_evolution.append(cash_in_hand)
        bet_evolution = []
        bet = initial_bet
        bet_evolution.append(initial_bet)
        attempt = 1
        for i in range(0,n):
            result = random.randint(0, 37) 
            if result == 0 :
                parity = 'n'
            elif result % 2 == 0:
                parity = 'p'
            else: parity = 'i'
            ##Evaluamos si tiene
            if(cash_in_hand != 0 or initial_capital == float('inf')):
                #evaluo si gano
                if parity != wagered :
                    cash_in_hand = cash_in_hand - bet
                    if(attempt == 1):
                        bet = initial_bet
                    else:
                        bet = bet_evolution[-2] + bet_evolution[-1]
                    attempt += 1
                else: 
                    winning_attempt.append(attempt)  
                    cash_in_hand = cash_in_hand + bet
                    attempt = 1
                    bet = initial_bet
            cash_evolution.append(cash_in_hand) 
            bet_evolution.append(bet)
            if bet>cash_in_hand and initial_capital != float('inf'):
                print('No alcanza para la proxima apuesta')
                bet = cash_in_hand
        cash_evolution_players.append(cash_evolution)
        print(cash_evolution)   
        winning_attempts.append(winning_attempt)
    # relative_frequency(winning_attempts)
    evolution(cash_evolution_players)


# fibonacci_strategy(1,1,100,10)