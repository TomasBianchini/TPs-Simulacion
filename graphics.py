import matplotlib.pyplot as plt

colores = ['r', 'g', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']

def cash_evolution(data):
    plt.figure(figsize=(10, 6))
    for i, player_data in enumerate(data):
        plt.plot(player_data)
    # plt.axhline(y=data[0], color='r', linestyle='--')
    plt.xlabel('tirada n')
    plt.ylabel('capital en mano')
    plt.grid(True)
    plt.show()

#Grafico de Fracuencia Relativa
def relative_frequency(winning_attemptAcc):
    plt.xlabel('Número')
    plt.ylabel('Frecuencia Relativa')
    plt.title('Frecuencia Relativa de Números en tiradaGanadora')
    number_frequency = {}  # Inicializamos un diccionario vacío para almacenar las frecuencias de cada número
    for attempt in winning_attemptAcc:
        for i in attempt:
            # Verificamos si el número ya está en el diccionario, si no, lo inicializamos con 0
            if i not in number_frequency:
                number_frequency[i] = 0
            # Incrementamos la frecuencia del número en 1
            number_frequency[i] += 1
    numbers = list(number_frequency.keys())
    frecuencias = list(number_frequency.values())
    total_attempts = sum(len(attempt) for attempt in winning_attemptAcc)
    relative_frequencies = [number_frequency[numero] / total_attempts for numero in numbers]
    plt.bar(numbers, relative_frequencies)
    plt.show()


#Grafico de variacion de capital
def GRAF_VARCAP(flujoCaja):
    plt.figure("Flujo de caja con respecto a N")
    plt.title("Flujo de caja con respecto a N")
    plt.xlabel("N (numero de tiradas")
    plt.ylabel("CC (cantidad de capital)")
    plt.axhline(y=0, color='b')
    plt.plot(range(1, len(flujoCaja) + 1), flujoCaja)
    plt.grid(True)
    plt.show()
  