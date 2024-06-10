import random
import math

def generar_pares_coprimos(n):
    pares_coprimos = []
    while len(pares_coprimos) < n:
        p = random.randint(1, 64)  # Genera un número aleatorio entre 1 y 100
        a=2**p
        b = random.randint(1, 10000)  # Genera otro número aleatorio entre 1 y 100
        if math.gcd(a, b) == 1:  # Si el MCD de a y b es 1, entonces son coprimos
            pares_coprimos.append((a, b))
    return pares_coprimos

# Genera una lista de 50 pares de números coprimos
pares_coprimos = generar_pares_coprimos(10)
for par in pares_coprimos:
    print(par)

