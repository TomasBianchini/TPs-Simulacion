import random 
import matplotlib
prom = 18
n = 1000 #TODO pasarlo a argumentos de entrada  
corridas = []
for j in range (0,100):
    frecuencia_absoluta = {}
    frecuencia_relativa = {}
    valores = [random.randint(0, 36) for _ in range(1000)]
    for i in range(0,37):
        frecuencia_absoluta[i] = valores.count(i)
        frecuencia_relativa[i] =  frecuencia_absoluta[i] / 1000
    # print("Valores generados:", valores)
    # for i in range(0, 37):
        # print("Frecuencia absoluta de ", i, ":", frecuencia_absoluta[i])
        # print("Frecuencia relativa de ", i, ":", frecuencia_relativa[i])
    corridas.append(frecuencia_absoluta)
print(corridas)

