import random
from graphics import GRAF_FREC_RELATIVA, GRAF_VARCAP
def labouchere_strategy(n, apuestaInicial, capital=float('inf')):
    print('Metodo Labouchere')
    i = 1
    tiradaGanadora = []
    flujoCaja = []
    apuestas = apuestaInicial.copy()  # Copiar la lista de apuestas iniciales
    flujoCaja.append(0)
    apuestas_iniciales = apuestaInicial.copy()  # Mantener una copia de la lista de apuestas iniciales
    
    while i <= n:
        
        apostado = 'p' # Apostar a la paridad par
        paridad = 'i'  # Empezar asumiendo una paridad diferente a la apostada
        tirada = 1
        
        
        while paridad != apostado and i <= n:
            apuesta = apuestas[0] if len(apuestas) == 1 else apuestas[0] + apuestas[-1] 
            i += 1  # Acumular un giro de ruleta
            valorGanador = random.randint(0, 36)   # Supongamos que hay una función tirarRuleta() que devuelve el valor ganador
            if valorGanador == 0:
                paridad = 'n'  # Si el valor ganador es 0, se considera como "nulo"
            elif valorGanador % 2 == 0:
                paridad = 'p'  # Si el valor ganador es par, la paridad es 'p'
            else:
                paridad = 'i'  # Si el valor ganador es impar, la paridad es 'i'
            
            # Evaluar si se ganó o se perdió
            if paridad != apostado:  # Pérdida
                flujoCaja.append(flujoCaja[-1] - apuesta)
                if len(apuestas) > 1:
                    apuestas.append(apuesta)  # Agregar la suma de la primera y última apuesta a la lista
                tirada += 1
            else:  # Ganancia
                tiradaGanadora.append(tirada)  # Guardar tirada ganadora
                flujoCaja.append(flujoCaja[-1] + apuesta)
                if len(apuestas) > 1:
                    apuestas.pop(0)  # Eliminar la primera apuesta
                    apuestas.pop(-1)  # Eliminar la última apuesta
            if not apuestas:  # Si la lista de apuestas está vacía, restaurarla a su estado original
                apuestas = apuestas_iniciales.copy()
            if (apuestas[0] + apuestas[-1] > capital) or capital + flujoCaja[-1] < 0 or -flujoCaja[-1]+(apuestas[0] + apuestas[-1]) > capital:
                print('Capital:', capital, 'Flujo de caja:', flujoCaja[-1], 'Apuesta futura:', (apuestas[0] + apuestas[-1]),'apuestas',apuestas)
                break  # Salir del bucle si el capital se agota o se alcanza el límite
        
        if(apuestas[0] + apuestas[-1] > capital) or capital + flujoCaja[-1] < 0 or -flujoCaja[-1]+(apuestas[0] + apuestas[-1]) > capital:
            print("Se alcanzó el límite de capital negativo. Salir del método.")
            break
    
    print('Flujo de caja:', flujoCaja)
    print('Tirada ganadora:', tiradaGanadora)
    GRAF_FREC_RELATIVA(tiradaGanadora)
    GRAF_VARCAP(flujoCaja)