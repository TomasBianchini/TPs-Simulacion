import numpy as np
from math import sqrt
from scipy.stats import norm
def runsTest(numbers: list, alpha: float = .05) -> str:
    mean_est = np.mean(numbers)
    sec = [1 if r > mean_est else 0 for r in numbers] # 1 si es mayor a la media, 0 si es menor
    c = 0
    for i in range(1, len(sec)):
        if sec[i-1] != sec[i]: 
            c += 1
    n_0 = sec.count(0) # Cantidad de 0
    n_1 = sec.count(1) # Cantidad de 1
    nn2 = 2*n_0*n_1 
    n = len(sec)
    mean = ((2 * n_1 * n_0) / (n_1 + n_0)) + 1 # Media
    if n_1 == 0 or n_0 == 0:
        return False
    var_c = (nn2*(nn2-n))/((n**2)*(n-1))
    z = (c-mean)/sqrt(var_c)
    return abs(z) < norm.ppf(1-alpha/2)






#Los generadores devuelven numeros pero se necesita trabajar con bits para el test de monobit
def number_to_bits(number):
    binary_representation = bin(number)[2:]
    padded_binary = binary_representation.zfill(8)
    bits_list = [int(bit) for bit in padded_binary]
    print('Número:', number, 'Representación binaria:', padded_binary)
    return bits_list
#FREQUENCY MONOBIT TEST
def monobit_test(sequence):
    bits_sequence = [number_to_bits(num) for num in sequence]
    flat_bits_sequence = [bit for sublist in bits_sequence for bit in sublist]
    ones_count = sum(1 for bit in flat_bits_sequence if bit == 1)
    zeros_count = len(flat_bits_sequence) - ones_count
    proportion_ones = ones_count / len(flat_bits_sequence)
    print('Proporción de unos:', proportion_ones)
    if proportion_ones >= 0.45 and proportion_ones <= 0.55:
        return "Pasa el Test de Frecuencia Monobit: Proporción de unos cercana a 0.5"
    else:
        return "No pasa el Test de Frecuencia Monobit: Proporción de unos no cercana a 0.5"

# Test chi cuadrado
def chi_test(numbers, k, alpha):
    n = len(numbers)
    #bins = np.linspace(0, 1, k + 1)
    bins= np.linspace(min(numbers), max(numbers), k + 1)
    hist, _ = np.histogram(numbers, bins)
    expected = n / k
    chi = sum([(observed - expected) ** 2 / expected for observed in hist])
    result = chi<norm.ppf(1-alpha, k-1)
    print("Resultado del test con una confianza del", (1 - alpha  ) * 100, "%:",
          "Pasa el test ChiCuad" if result else "No pasa el test ChiCuad")
    return result



h = monobit_test( [100000,1116544556151561,156154,51,1,515])
print(h)