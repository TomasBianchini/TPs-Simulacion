import numpy   
from scipy.special import gammaincc


def longest_run_test(binary_data):
    size_data = len(binary_data)
    if size_data < 128:
        return ("No hay suficientes tados para realizar el test segun NEST")
    elif size_data < 6272:
        k, m = 3, 8
        v_values = [1, 2, 3, 4]
        pik_values = [0.21484375, 0.3671875, 0.23046875, 0.1875]
    elif size_data < 75000:
        k, m = 5, 128
        v_values = [4, 5, 6, 7, 8, 9]
        pik_values = [0.1174035788, 0.242955959, 0.249363483, 0.17517706, 0.102701071, 0.112398847]
    else:
        k, m = 6, 10000
        v_values = [10, 11, 12, 13, 14, 15, 16]
        pik_values = [0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727]
    
     #Divido los bloques de tamaño M
        
    start=0
    end = m
    n = size_data//m
    values_max_block = numpy.zeros(n,dtype=int)
    frequencies = numpy.zeros(k + 1)
    for i in range (n):
            block_data = binary_data[start:end] 
            #Cuento el numero de 1s que tiene el bloque
            actual_count, max_count = 0,0
            for j in range(0,m):
                if block_data[j]== 1 :   #DUDA: Vienen como string o como number?
                    actual_count += 1
                    max_count = max(actual_count, max_count) 
                else:
                    max_count = max(actual_count, max_count)
                    actual_count = 0
            values_max_block[i] = max_count #Para cada bloque guardo la secuencia de 1s mas larga
            #ASINGO LAS FRECUENCIAS SEGUN LOS Valores DADOS POR NIST ¿¿?? (Sale de la tablita del PDF)
            if max_count <= v_values[0]:
                frequencies[0] += 1  
            for j in range(k):
                if max_count == v_values[j]:
                    frequencies[j] += 1
            if max_count > v_values[k - 1]:
                frequencies[k] += 1
            start += m
            end += m

            #Computo la prueba CHI CUADRADO segun los valores dados por nist. 
    chi_sq = 0
    for i in range (len(frequencies)):
        chi_sq += pow(v_values[i]- n*pik_values[i],2)/(n*pik_values[i])
        #p_value = stats.chisquare(chi_sq,k)
        p_value= gammaincc((k/2),(chi_sq/2))

    #Analizamos el resultado:
    if p_value < 0.01:
        return ("La secuencia no es random. No pasa el test de la secuencia mas larga de unos.")
    else: 
        return( "La secuencia es random segun el test." )