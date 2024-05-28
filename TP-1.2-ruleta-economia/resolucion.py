import sys
import matplotlib.pyplot as plt
import random

#GRAFICAS
colores = ['r', 'g', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']

def cash_evolution(data):
    plt.figure(figsize=(10, 6))
    for i, player_data in enumerate(data):
        plt.plot(player_data)
    # plt.axhline(y=data[0], color='r', linestyle='--')
    plt.xlabel('tirada n')
    plt.ylabel('capital en mano')
    plt.grid(True)
    plt.show()

#Grafico de Fracuencia Relativa
def relative_frequency(winning_attemptAcc):
    plt.xlabel('Número')
    plt.ylabel('Frecuencia Relativa')
    plt.title('Frecuencia Relativa de Números en tiradaGanadora')
    number_frequency = {}  # Inicializamos un diccionario vacío para almacenar las frecuencias de cada número
    for attempt in winning_attemptAcc:
        for i in attempt:
            # Verificamos si el número ya está en el diccionario, si no, lo inicializamos con 0
            if i not in number_frequency:
                number_frequency[i] = 0
            # Incrementamos la frecuencia del número en 1
            number_frequency[i] += 1
    numbers = list(number_frequency.keys())
    frecuencias = list(number_frequency.values())
    total_attempts = sum(len(attempt) for attempt in winning_attemptAcc)
    relative_frequencies = [number_frequency[numero] / total_attempts for numero in numbers]
    plt.bar(numbers, relative_frequencies)
    plt.show()


#Grafico de variacion de capital
def GRAF_VARCAP(flujoCaja):
    plt.figure("Flujo de caja con respecto a N")
    plt.title("Flujo de caja con respecto a N")
    plt.xlabel("N (numero de tiradas")
    plt.ylabel("CC (cantidad de capital)")
    plt.axhline(y=0, color='b')
    plt.plot(range(1, len(flujoCaja) + 1), flujoCaja)
    plt.grid(True)
    plt.show()

#METODO Fibonacci
def fibonacci_strategy(number_of_players, initial_bet, n ,initial_capital = float('inf')):
    print('Metodo Fibonacci')
    winning_attempts = []
    cash_flow_players = []
    wagered  = 'p' #PAR
    for j in range(0,number_of_players):
        winning_attempt = []
        cash_flow = []
        cash_in_hand = initial_capital if initial_capital != float('inf') else 0
        cash_flow.append(cash_in_hand)
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
            cash_flow.append(cash_in_hand) 
            bet_evolution.append(bet)
            if bet>cash_in_hand and initial_capital != float('inf'):
                print('No alcanza para la proxima apuesta')
                bet = cash_in_hand
        cash_flow_players.append(cash_flow) 
        winning_attempts.append(winning_attempt)
    relative_frequency(winning_attempts)
    cash_evolution(cash_flow_players)
##METODO MARTINGALA
def martingala_strategy(number_of_players, initial_bet,n, initial_capital=float('inf')):
    print('Metodo Martingala')
    Winning_AttemptAcc = []
    cash_evolution_pl_players = []
    all_bets=[]
    for p in range(0,number_of_players):
        cash_in_hand = initial_capital if initial_capital != float('inf') else 0
        winning_attempt = []
        cash_evolution_pl = []
        cash_evolution_pl.append(cash_in_hand)
        win_at = 1
        bet=initial_bet 
        bets=[bet]
        for i in range(0, n):
            
            apostado = 'p' # Apostar a la paridad par
            result = random.randint(0, 37)
                # Supongamos que hay una función tirarRuleta() que devuelve el valor ganador
            if result == 0:
                paridad = 'n'  # Si el valor ganador es 0, se considera como "nulo"
            elif result % 2 == 0:
                paridad = 'p'  # Si el valor ganador es par, la paridad es 'p'
            else:
                paridad = 'i'  # Si el valor ganador es impar, la paridad es 'i'
            
            # Evaluar si se ganó o se perdió
            if cash_evolution_pl[-1] != 0 or initial_capital == float('inf'):
                if paridad != apostado:  # Pérdida
                    cash_in_hand=cash_in_hand-bet 
                    bet = 2*bet
                    win_at += 1
                else:  # Ganancia
                    winning_attempt.append(win_at)  # Guardar win_at ganadora
                    cash_in_hand=cash_in_hand+bet
                    win_at = 1
                    bet = initial_bet
            cash_evolution_pl.append(cash_in_hand)
            bets.append(bet)
            #si no ta alcanza para la proxima apuesta, apuesto lo que me queda
            if bet>cash_in_hand and initial_capital != float('inf'):
                bet = cash_in_hand
        
        cash_evolution_pl_players.append(cash_evolution_pl)
        Winning_AttemptAcc.append(winning_attempt)
        all_bets.append(bets)
    relative_frequency(Winning_AttemptAcc)
    cash_evolution(cash_evolution_pl_players)
##METODO DALEMBERT 
def dalembert_strategy(number_of_players, initial_bet,n, initial_capital=float('inf')):
    print('Metodo DAlembert')
    Winning_AttemptAcc = []
    cash_evolution_pl_players = []
    all_bets=[]
    for p in range(0,number_of_players):
        cash_in_hand = initial_capital if initial_capital != float('inf') else 0
        winning_attempt = []
        cash_evolution_pl = []
        cash_evolution_pl.append(cash_in_hand)
        win_at = 1
        bet=initial_bet 
        bets=[bet]
        for i in range(0, n):
            
            apostado = 'p' # Apostar a la paridad par
            result = random.randint(0, 37)
                # Supongamos que hay una función tirarRuleta() que devuelve el valor ganador
            if result == 0:
                paridad = 'n'  # Si el valor ganador es 0, se considera como "nulo"
            elif result % 2 == 0:
                paridad = 'p'  # Si el valor ganador es par, la paridad es 'p'
            else:
                paridad = 'i'  # Si el valor ganador es impar, la paridad es 'i'
            
            # Evaluar si se ganó o se perdió
            if cash_evolution_pl[-1] != 0 or initial_capital == float('inf'):
                if paridad != apostado:  # Pérdida
                    cash_in_hand=cash_in_hand-bet 
                    bet += 1
                    win_at += 1
                else:  # Ganancia
                    winning_attempt.append(win_at)  # Guardar win_at ganadora
                    cash_in_hand=cash_in_hand+bet
                    win_at = 1
                    if bet > 1:
                      bet -= 1
            cash_evolution_pl.append(cash_in_hand)
            bets.append(bet)
            #si no ta alcanza para la proxima apuesta, apuesto lo que me queda
            if bet>cash_in_hand and initial_capital != float('inf'):
                bet = cash_in_hand
        
        cash_evolution_pl_players.append(cash_evolution_pl)
        Winning_AttemptAcc.append(winning_attempt)
        all_bets.append(bets)
    relative_frequency(Winning_AttemptAcc)
    cash_evolution(cash_evolution_pl_players)    

##METODO LABOUCHERE
def labouchere_strategy(number_of_players, initial_bet,n, initial_capital=float('inf')):
    print('Metodo Labouchere')
    Winning_AttemptAcc = []
    cash_evolution_pl_players = []
    all_bets=[]
    for p in range(0,number_of_players):
        cash_in_hand = initial_capital if initial_capital != float('inf') else 0
        winning_attempt = []
        cash_evolution_pl = []
        bets = initial_bet.copy()  # Copiar la lista de bets iniciales
        cash_evolution_pl.append(cash_in_hand)
        win_at = 1
        bet=bets[0] + bets[-1] 
        bets_history=[bet]
        for i in range(0, n):
            apostado = 'p' # Apostar a la paridad par
            result = random.randint(0, 37)
                # Supongamos que hay una función tirarRuleta() que devuelve el valor ganador
            if result == 0:
                paridad = 'n'  # Si el valor ganador es 0, se considera como "nulo"
            elif result % 2 == 0:
                paridad = 'p'  # Si el valor ganador es par, la paridad es 'p'
            else:
                paridad = 'i'  # Si el valor ganador es impar, la paridad es 'i'
            # Evaluar si se ganó o se perdió
            if cash_evolution_pl[-1] != 0 or initial_capital == float('inf'):
                if paridad != apostado:  # Pérdida
                    cash_in_hand=cash_in_hand-bet 
                    bets.append(bet)  # Agregar la suma de la primera y última bet a la lista
                    win_at += 1
                else:  # Ganancia
                    winning_attempt.append(win_at)  # Guardar win_at ganadora
                    cash_in_hand=cash_in_hand+bet
                    win_at = 1
                    if len(bets) > 1:
                        bets.pop(0)  # Eliminar la primera bet
                        bets.pop(-1)  # Eliminar la última bet
                    else:
                        bets.pop(0)  # Eliminar la única bet
            cash_evolution_pl.append(cash_in_hand)
            bets_history.append(bet)
            if not bets:  # Si la lista de bets está vacía, restaurarla a su estado original
                bets = initial_bet.copy() 
            bet = bets[0] if len(bets) == 1 else bets[0] + bets[-1] # Calcular la próxima bet
            #si no ta alcanza para la proxima apuesta, apuesto lo que me queda
            if bet>cash_in_hand and initial_capital != float('inf'):
                bet = cash_in_hand
        
        cash_evolution_pl_players.append(cash_evolution_pl)
        Winning_AttemptAcc.append(winning_attempt)
        all_bets.append(bets_history)
    relative_frequency(Winning_AttemptAcc)
    cash_evolution(cash_evolution_pl_players)

##MAIN
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
