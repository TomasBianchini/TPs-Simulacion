import numpy as np
from math import sqrt
from scipy.stats import norm
import scipy.special


#frequency_monobit_test
def frequency_monobit_test(bit_sequence: str):
    n = len(bit_sequence)
    s = sum([1 if bit == '1' else -1 for bit in bit_sequence])
    s_obs = s / sqrt(n)
    p_value = scipy.special.erfc(abs(s_obs) / sqrt(2))
    print("p_value:", p_value)
    if p_value >= 0.01:
        print("Pasa el Test de Frecuencia Monobit")
    else:
        print("No pasa el Test de Frecuencia Monobit")

#runs_test
def runs_test(bit_sequence: str):
    n = len(bit_sequence)
    pi = bit_sequence.count('1') / n
    V_n_obs = 1 + sum(bit_sequence[i] != bit_sequence[i + 1] for i in range(n - 1))
    numerator = abs(V_n_obs - 2 * n * pi * (1 - pi))
    denominator = 2 * pi * (1 - pi) * np.sqrt(2 * n)
    p_value = scipy.special.erfc(numerator / denominator)
    print("p_value:", p_value)
    if p_value >= 0.01:
        print("Pasa el Test de Pruebas de Rachas")
    else:
        print("No pasa el Test de Pruebas de Rachas")




#Los generadores devuelven numeros pero se necesita trabajar con bits para el test de monobit
def number_to_bits(number):
    binary_representation = bin(number)[2:]
    padded_binary = binary_representation.zfill(8)
    bits_list = [int(bit) for bit in padded_binary]
    #print('Número:', number, 'Representación binaria:', padded_binary)
    return bits_list






# Test chi cuadrado
def chi_test(numbers, k, alpha):
    n = len(numbers)
    bins = np.linspace(0, 1, k + 1)
    #bins= np.linspace(min(numbers), max(numbers), k + 1)
    hist, _ = np.histogram(numbers, bins)
    expected = n / k
    chi = sum([(observed - expected) ** 2 / expected for observed in hist])
    result = chi<norm.ppf(1-alpha, k-1)
    print("Resultado del test con una confianza del", (1 - alpha  ) * 100, "%:",
          "Pasa el test ChiCuad" if result else "No pasa el test ChiCuad")
    return result



# h = monobit_test( [100000,1116544556151561,156154,51,1,515])
# print(h)



#testing frequency_monobit_test
bit_sequence = '1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000'
frequency_monobit_test(bit_sequence)

#testing runs_test
bit_sequence = '1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000'
runs_test(bit_sequence)