import numpy as np
from math import sqrt
from scipy.stats import norm
import scipy.special
from scipy.stats import chi2


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






#chi_square_test
def chi_square_test(sequence, confidence_level):
    n = len(sequence)
    m = int(sqrt(n))

    expected_frequency = len(sequence) / m

    interval_size = 1.0 / m
    bin_edges = [i * interval_size for i in range(m + 1)]
    observed_frequencies, _ = np.histogram(sequence, bins=bin_edges)

    chi_square_stat = sum((observed_frequencies - expected_frequency) ** 2 / expected_frequency)
    degrees_of_freedom = m - 1
    critical_value = chi2.ppf(confidence_level, degrees_of_freedom)

    if chi_square_stat < critical_value:
        print("La secuencia pasa la prueba Chi-cuadrado.")
    else:
        print("La secuencia no pasa la prueba Chi-cuadrado.")




#testing chi_square_test
sequence = [
    0.347, 0.832, 0.966, 0.472, 0.797, 0.101, 0.696, 0.966, 0.404, 0.603,
    0.993, 0.371, 0.729, 0.067, 0.189, 0.977, 0.843, 0.562, 0.549, 0.992,
    0.674, 0.628, 0.055, 0.494, 0.494, 0.235, 0.178, 0.775, 0.797, 0.252,
    0.426, 0.054, 0.022, 0.742, 0.674, 0.898, 0.641, 0.674, 0.821, 0.19,
    0.46, 0.224, 0.99, 0.786, 0.393, 0.461, 0.011, 0.977, 0.246, 0.881,
    0.189, 0.753, 0.73, 0.797, 0.292, 0.876, 0.707, 0.562, 0.562, 0.821,
    0.112, 0.191, 0.584, 0.347, 0.426, 0.057, 0.819, 0.303, 0.404, 0.64,
    0.37, 0.314, 0.731, 0.742, 0.213, 0.472, 0.641, 0.944, 0.28, 0.663,
    0.909, 0.764, 0.999, 0.303, 0.718, 0.933, 0.056, 0.415, 0.819, 0.444,
    0.178, 0.516, 0.437, 0.393, 0.268, 0.123, 0.945, 0.527, 0.459, 0.652
]

chi_square_test(sequence, 0.95)


#testing frequency_monobit_test
#bit_sequence = '1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000'
#frequency_monobit_test(bit_sequence)

#testing runs_test
#bit_sequence = '1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000'
#runs_test(bit_sequence)