from test import RunsTest, monobit_test

def generatorLGC(seed, mult, mod,inc, m) -> list:
    # Linear congruential generator
    numbers = [seed] # No se si es necesario agregar la semilla a la lista
    for i in range(m):
        next_number = ((mult*numbers[i])+inc) % mod
        numbers.append(next_number)
    return numbers
h = generatorLGC(1, 1664525, 2**32 , 1013904223,10)
print(h)
mod = 2**32
normalized_numbers = [num / mod for num in h]
print (normalized_numbers)
h2 = RunsTest(h)
print(h2)
h3 = monobit_test(normalized_numbers)
print(h3)


# Metodo de los cuadrados medios #
def AlgorithmMiddleSquare(seed: int, n: int) -> list:
    """
    Inputs:
        seed: int || seed should be at least 4 digits long
        n: int || number of random numbers to generate
    Output:
        list || n sized random number list
    """
    if len(str(seed)) < 4:
        raise ValueError("Seed should be at least 4 digits long")

    r_i = []
    X_n = seed
    D = len(str(seed))
    
    for i in range(n):
        X_n = X_n ** 2
        str_X_n = str(X_n).zfill(2 * D)
        middle_digits = str_X_n[D//2 : D + D//2]
        X_n = int(middle_digits)
        r_i.append(X_n)

    return r_i

# Ejemplo de uso

h = AlgorithmMiddleSquare(82173, 100)
print(h)
mod = 2**32
normalized_numbers = [num / mod for num in h]
print (normalized_numbers)
h2 = RunsTest(h)
print(h2)
h3 = monobit_test(normalized_numbers)
print(h3)