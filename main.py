import sys
from fibonacci_strategy import fibonacci_strategy
from martingala_strategy_viejo import martingala_strategy 
from dalembert_strategy_viejo import dalembert_strategy
from martingala_strategy import martingala_strategy 
from dalembert_strategy import dalembert_strategy
from labouchere_strategy import labouchere_strategy

if len(sys.argv) != 11 or sys.argv[1] != "-j" or sys.argv[3] != "-b" or sys.argv[5] != "-n" or sys.argv[7] != "-c" or sys.argv[9] != "-s":
    print("Uso: python programa.py -j <cant_jugadores> -b <apuesta_inicial> -n <cant_tiradas> -c <capital_inicial(0 si es infinito)> -s <estrategia>")
    sys.exit(1)

number_of_players = int(sys.argv[2])
initial_bet = int(sys.argv[4])
n = int(sys.argv[6])
capital = int(sys.argv[8])
strategy = sys.argv[10] # f- fibonacci, m- martingala, d- dalembert, l- labouchere

if strategy == 'f':
    if capital != 0:
        fibonacci_strategy(number_of_players, initial_bet, n, capital)
    else:
        fibonacci_strategy(number_of_players, initial_bet, n) 
elif strategy == 'm':
    if capital != 0:
        martingala_strategy(number_of_players, initial_bet, n, capital)
    else:
        martingala_strategy(number_of_players, initial_bet, n)
elif strategy == 'd':
    if capital != 0:
        dalembert_strategy(number_of_players, initial_bet, n, capital)
    else:
        dalembert_strategy(number_of_players, initial_bet, n)
elif strategy == 'l':
    data = [initial_bet,initial_bet,initial_bet,initial_bet ]
    if capital != 0:
        labouchere_strategy(number_of_players, data, n, capital)
    else:
        labouchere_strategy(number_of_players, data, n)