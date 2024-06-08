from test import medianTest, monobit_test, chi_test
from graph import plot_scatter, create_bitmap_image



def generatorLGC(seed, a, m,c, n) -> list:
    # Linear congruential generator
    numbers = [] # No se si es necesario agregar la semilla a la lista
    for i in range(n):
        if i==0:
            next_number = ((a*seed)+c) % m
        else:
            next_number = ((a*numbers[i-1])+c) % m
        numbers.append(next_number)
        probabilities = [number / (m-1) for number in numbers]  # Excluimos la semilla de la lista final
    return probabilities


# Metodo de los cuadrados medios #
def AlgorithmMiddleSquare(seed: int, n: int) -> list:
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
        r_i.append(X_n / (10 ** D))
    return r_i

