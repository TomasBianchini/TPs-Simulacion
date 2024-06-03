import numpy as np
from math import sqrt
from scipy.stats import norm
def RunsTest(numbers: list, alpha: float = .05) -> str:
    media_est = np.mean(numbers)
    sec = [1 if r > media_est else 0 for r in numbers] # 1 si es mayor a la media, 0 si es menor
    c = 0
    for i in range(1, len(sec)-1):
        if sec[i-1] != sec[i]: 
            c += 1
    n_0 = sec.count(0) # Cantidad de 0
    n_1 = sec.count(1) # Cantidad de 1
    nn2 = 2*n_0*n_1 
    n = len(sec)
    mean_c = .5+(nn2/n) # Media
    if n_1 == 0 or n_0 == 0:
        return False
    var_c = (nn2*(nn2-n))/((n**2)*(n-1))
    z = (c-mean_c)/sqrt(var_c)
    return abs(z) < norm.ppf(1-alpha/2)






#Los generadores devuelven numeros pero se necesita trabajar con bits para el test de monobit
def number_to_bits(number):
    binary_representation = bin(number)[2:]
    padded_binary = binary_representation.zfill(8)
    bits_list = [int(bit) for bit in padded_binary]
    return bits_list
#FREQUENCY MONOBIT TEST
def monobit_test(sequence):
    bits_sequence = [number_to_bits(num * 10000) for num in sequence]
    flat_bits_sequence = [bit for sublist in bits_sequence for bit in sublist]
    ones_count = sum(1 for bit in flat_bits_sequence if bit == 1)
    zeros_count = len(flat_bits_sequence) - ones_count
    proportion_ones = ones_count / len(flat_bits_sequence)
    print('Proporción de unos:', proportion_ones)
    if proportion_ones >= 0.45 and proportion_ones <= 0.55:
        return "Pasa el Test de Frecuencia Monobit: Proporción de unos cercana a 0.5"
    else:
        return "No pasa el Test de Frecuencia Monobit: Proporción de unos no cercana a 0.5"
