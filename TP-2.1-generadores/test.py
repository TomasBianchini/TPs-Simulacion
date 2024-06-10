import numpy as np
from math import sqrt
from scipy.stats import norm
import scipy.special
from scipy.stats import chi2 
from scipy.special import gammaincc

#frequency_monobit_test
def frequency_monobit_test(bit_sequence: str):
    n = len(bit_sequence)
    s = sum([1 if bit == '1' else -1 for bit in bit_sequence])
    s_obs = s / sqrt(n)
    p_value = scipy.special.erfc(abs(s_obs) / sqrt(2))
    print("p_value:", p_value)
    if p_value >= 0.01:
        print("Pasa la prueba de frecuencia monobit.")
    else:
        print("No pasa la prueba de frecuencia monobit.")

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
        print("Pasa la prueba de rachas.")
    else:
        print("No pasa la prueba de rachas.")




#Los generadores devuelven numeros pero se necesita trabajar con bits para el test de monobit
def number_to_bits(number):
    binary_representation = bin(number)[2:]
    padded_binary = binary_representation.zfill(8)
    bits_list = [int(bit) for bit in padded_binary]
    #print('Número:', number, 'Representación binaria:', padded_binary)
    return bits_list


#longest_run_test
def longest_run_test(bit_sequence):
    h = []
    for b in bit_sequence: h.append(int(b))

    size_data = len(h)
    if size_data < 128:
        return ("No hay suficientes tados para realizar el test segun NEST")
    elif size_data < 6272:
        k, m = 3, 8
        v_values = [1, 2, 3, 4]
        #pik_values = [0.21484375, 0.3671875, 0.23046875, 0.1875]
        pik_values = [0.2148, 0.3672, 0.2305, 0.1875]
    elif size_data < 75000:
        k, m = 5, 128
        v_values = [4, 5, 6, 7, 8, 9]
        #pik_values = [0.1174035788, 0.242955959, 0.249363483, 0.17517706, 0.102701071, 0.112398847]
        pik_values = [0.1174, 0.2430, 0.2493, 0.1752, 0.1027, 0.1124]
    else:
        k, m = 6, 10000
        v_values = [10, 11, 12, 13, 14, 15, 16]
        pik_values = [0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727]
    
    start=0
    end = m
    n = size_data//m
    values_max_block = np.zeros(n,dtype=int)
    frequencies = np.zeros(k + 1)
    for i in range (n):
            block_data = h[start:end] 
            actual_count, max_count = 0,0
            for j in range(m):
                if block_data[j]==1 :
                    actual_count += 1
                    max_count = max(actual_count, max_count) 
                else:
                    max_count = max(actual_count, max_count)
                    actual_count = 0
            values_max_block[i] = max_count
            if max_count <= v_values[0]:
                frequencies[0] += 1  
            for j in range(1,k):
                if max_count == v_values[j]:
                    frequencies[j] += 1
            if max_count > v_values[k - 1]:
                frequencies[k] += 1
            start += m
            end += m

    chi_square=0
    for i in range (len(frequencies)):
        chi_square += ((frequencies[i]- n*pik_values[i])**2)/(n*pik_values[i])

  
    p_value= gammaincc((k/2),(chi_square/2))
    #print('P_VALUE:' , p_value)
    #print ('CHI_SQ:', chi_square)
    #print('Cant Bloques:',n)
    #print('M: ', m)
    #print('K: ', k)

    #Analizamos el resultado:
    if p_value < 0.01:
        print("NO pasa la prueba Test de Cantidad de Unos por Bloque")
    else: 
        print( "SI Pasa la prueba Test de Cantidad de Unos por Bloque" )


#chi_square_test
def chi_square_test(decimal_sequence, confidence_level):
    n = len(decimal_sequence)
    m = int(sqrt(n))

    expected_frequency = len(decimal_sequence) / m

    interval_size = 1.0 / m
    bin_edges = [i * interval_size for i in range(m + 1)]
    observed_frequencies, _ = np.histogram(decimal_sequence, bins=bin_edges)

    chi_square_stat = sum((observed_frequencies - expected_frequency) ** 2 / expected_frequency)
    degrees_of_freedom = m - 1
    critical_value = chi2.ppf(confidence_level, degrees_of_freedom)

    if chi_square_stat < critical_value:
        print("Pasa la prueba de Chi-cuadrado. ") #No se puede afirmar que no sigue una distribucion uniforme
    else:
        print("NO pasa la prueba de Chi-cuadrado.")


def generator_to_tests(numbers_generated):
    h5 = []
    """ decimal = []
    for i in numbers_generated:
        decimal.append(int(i*10000))
    print (decimal)  """
    for i in numbers_generated:
        h5.extend(number_to_bits(int(i*10000)))
    return(h5)

def array_to_string(bits_array):
    bits_array = list(map(str, bits_array))
    cadena = ''.join(bits_array)
    return cadena





#testing frequency_monobit_test
'''
bit_sequence = '1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000'
frequency_monobit_test(bit_sequence)
'''

#testing runs_test
'''
bit_sequence = '1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000'
runs_test(bit_sequence)
'''

#testing longest_run_test
'''
bit_sequence = '11001100000101010110110001001100111000000000001001001101010100010001001111010110100000001101011111001100111001101101100010110010'
longest_run_test(bit_sequence)
'''

#testing chi_square_test
'''
decimal_sequence = [
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
#chi_square_test(decimal_sequence, 0.95)
'''