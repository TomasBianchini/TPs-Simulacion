#Test for the Longest Runs of Ones in a Block

def longest_run_test(binary_data):
    #Definimos bloques de tamaño M
    m=128
    size_data = len(binary_data) #SALEN DE LA TABLA PAG 56
    if (size_data<6272) :
        return "La cantidad de datos no es suficiente."
    else:
        #Divido los bloques de tamaño M
        start=0
        end = m
        size = m
        values_max_block = []
        for i in range (size_data//m):
            block_data = binary_data[start:end] 
            #Cuento el numero de 1s que tiene el bloque
            actual_count, max_count = 0
            for j in range(0,m):
                if block_data[j]== 1 :   #DUDA: Vienen como string o como number?
                    actual_count += 1
                    max_count = max(actual_count, max_count) 
                else:
                    max_count = max(actual_count, max_count)
                    actual_count = 0
            values_max_block[i] = max_count #Para cada bloque guardo la secuencia de 1s mas larga
        




        return 5