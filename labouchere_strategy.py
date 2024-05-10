import random
from graphics import cash_evolution, relative_frequency
def labouchere_strategy(number_of_players, initial_bet,n, initial_capital=float('inf')):
    print('Metodo Labouchere')
    Winning_AttemptAcc = []
    cash_evolution_pl_players = []
    for p in range(0,number_of_players):
        cash_in_hand = initial_capital if initial_capital != float('inf') else 0
        winning_attempt = []
        cash_evolution_pl = []
        bets = initial_bet.copy()  # Copiar la lista de bets iniciales
        cash_evolution_pl.append(cash_in_hand)
        win_at = 1
        bet=bets[0] + bets[-1] 
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
            if not bets:  # Si la lista de bets está vacía, restaurarla a su estado original
                bets = initial_bet.copy() 
            bet = bets[0] if len(bets) == 1 else bets[0] + bets[-1] # Calcular la próxima bet
            #si no ta alcanza para la proxima apuesta, apuesto lo que me queda
            if bet>cash_in_hand and initial_capital != float('inf'):
                bet = cash_in_hand
        
        cash_evolution_pl_players.append(cash_evolution_pl)
        Winning_AttemptAcc.append(winning_attempt)
        print('Flujo de caja:', cash_evolution_pl)
        print('win_at ganadora:', winning_attempt)
    
    print(cash_evolution_pl_players)
    relative_frequency(Winning_AttemptAcc)
    cash_evolution(cash_evolution_pl_players)

# labouchere_strategy(3, [1, 2, 3, 4], 100,20)