def generatorLGC(seed, mult, mod,inc, m) -> list:
    # Linear congruential generator
    numbers = [seed] # No se si es necesario agregar la semilla a la lista
    for i in range(m):
        next_number = ((mult*numbers[i])+inc) % mod
        numbers.append(next_number)
    return numbers
h = generatorGLC(1, 1664525, 2**32 , 1013904223,10)
print(h)