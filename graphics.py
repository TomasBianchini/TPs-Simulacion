import matplotlib.pyplot as plt

colores = ['r', 'g', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']

def cash_evolucion(data):
    plt.figure(figsize=(10, 6))
    for i, player_data in enumerate(data):
        plt.plot(player_data)
    plt.xlabel('tirada n')
    plt.ylabel('capital en mano')
    plt.grid(True)
    plt.show()


    

#Grafico de Fracuencia Relativa
def GRAF_FREC_RELATIVA(tiradaGanadoraAcum):
    plt.xlabel('Número')
    plt.ylabel('Frecuencia Relativa')
    plt.title('Frecuencia Relativa de Números en tiradaGanadora')
    
    frecuencia_numeros = {}  # Inicializamos un diccionario vacío para almacenar las frecuencias de cada número
    for tirada in tiradaGanadoraAcum:
        for i in tirada:
            # Verificamos si el número ya está en el diccionario, si no, lo inicializamos con 0
            if i not in frecuencia_numeros:
                frecuencia_numeros[i] = 0
            # Incrementamos la frecuencia del número en 1
            frecuencia_numeros[i] += 1
    numeros = list(frecuencia_numeros.keys())
    frecuencias = list(frecuencia_numeros.values())
    total_tiradas = sum(len(tirada) for tirada in tiradaGanadoraAcum)

    frecuencias_relativas = [frecuencia_numeros[numero] / total_tiradas for numero in numeros]


    plt.bar(numeros, frecuencias_relativas)
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
  