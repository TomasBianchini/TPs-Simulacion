from distribuciones import *
'''
#Distribucion UNIFORME (grafica muestra la probabilidad de cada numero)
print("Ejemplo de Uniforme (4,10)") #limite inferior, limite superior
print(uniformDistribution(4,10))

#Distribucion EXPONENCIAL
print("Ejemplo de Exponencial (0.5)") #E(x) = 1/a
print(exponentialDistribution(0.5))

#Distribucion GAMMA
print("Ejemplo de Gamma (10,3)") #cantidad de variables, tiempo entre eventos
print(gammaDistribution(10,3,100))

#Distribucion NORMAL
print("Ejemplo de Normal (100, 10)")#media, desviacion estandar
print(normalDistribution(100,3,1000))

#Distribucion PASCAL
print("Ejemplo de Pascal (100, 0.3)") #cantidad de variables, probabilidad de exito
pascalDistribution(100, 0.3, 1000)

#Distribucion BINOMIAL
print("Ejemplo de Binomial ((10,0.2,7))")#cantidad de variables, probabilidad de exito, intentos
print(binomialDistribution(10,0.4,100))

#Distribucion HIPERGEOMETRICA
print("Ejemplo de Hipergeometrica (100,26,0.5,10)")#poblacion de tn elementos ,muestra de ns elementos, probabilidad de exito, intentos
print(hypergeometricDistribution(100,26,0.5,100))

#Distribucion POISSON
print("Ejemplo de Poisson (5,100,10)")#lamda, cantidad de variables, intentos
print(dis_poisson(5,100,1000))
'''
