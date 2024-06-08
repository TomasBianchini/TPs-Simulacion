

#GCL_generator
def GCL_generator(seed, a, m,c, n) -> list:
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


#medium_square_generator
def medium_square_generator(seed: int, n: int) -> list:
    D = len(str(seed))
    if D <= 3:
        raise ValueError("La semilla debe ser de al menos 4 dígitos")
    
    ri_list = []
    Xi = seed

    for i in range(n):
        Yi = Xi ** 2
        str_Yi = str(Yi)
        
        if (len(str_Yi) % 2 != 0) and (len(str_Yi) >= 3):
            str_Yi = '0' + str_Yi

        if len(str_Yi) < 3:
            str_Yi = str_Yi.zfill(4)

        start_index = (len(str_Yi) // 2) - 2
        Xi = str_Yi[start_index : start_index + 4]
        ri = float('0' + '.' + Xi)
        ri_list.append(ri)
        Xi = int(Xi)
    
    return ri_list


# testing medium_square_generator
# print(medium_square_generator(5735, 5))
