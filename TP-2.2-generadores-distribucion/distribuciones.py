import numpy as np
import math
import random
from graph import *

def uniformDistribution(a,b): #limite inferior, limite superior
        r = np.random.uniform(0,1,100)
        x = a + (b-a)*r
        relative(x)
        return x

def exponentialDistribution(a): #E(x) = 1/a,n = cantidad de variables
        r = np.random.uniform(0,1,100)
        array = []
        x = -(1/a) * np.log(r)
        grafica(r,x)
        return x

def gammaDistribution(k,a,n): #cantidad de variables, tiempo entre eventos
        array = []
        for i in range(n):
            r = np.random.uniform(0,1,k) 
            tr = np.prod(r) 
            x = -math.log(tr) / a
            array.append(x)
        grafica_gamma(array, k, a)
        return array

def normalDistribution(mu,sigma, n): #media, desviacion estandar
        array = []
        for i in range(n):
            r = np.random.uniform(0,1,12)
            x = mu + sigma * (sum(r) - 6)
            array.append(x)
        grafica_normal(array, mu, sigma)
        return array

def pascalDistribution(k,q,n): #cantidad de variables, probabilidad de exito
        array = []
        for i in range(n):
            r = np.random.uniform(0,1,k)
            tr = np.prod(r)
            x = math.log(tr) / math.log(q)
            array.append(x)
        graficar_pascal(array,n)
        return array
        
def binomialDistribution(n,p,i): #cantidad de variables, probabilidad de exito, intentos 
        array = []
        for j in range(i):
            x = 0
            r = np.random.uniform(0,1,n)
            tr = 1
            for num in r:
                if num < p:
                    x += 1
            array.append(x) 
        graficar_binomial(array,n)
        return array

def hypergeometricDistribution(tn, ns, prob, i): #tn= poblacion de tn elementos ,ns = muestra de ns elementos, p = probabilidad de exito, i = intentos
        array = []
        for j in range(i):
            p= prob
            tnn = tn
            x=0
            r = np.random.uniform(0,1,tn)
            index = 0
            for i in range (ns):
                index += 1
                s=0
                if r[index] > p:
                        x+=1
                        s=1
                p=(tnn*p-s)/(tnn-1)
                tnn = tnn-1
            array.append(x)
        graficar_hypergeometric(array, ns)
        return array


def poissonDistribution(p,n,int): #lamda, cantidad de variables, intentos
    b = math.exp(-p)
    array = []
    for i in range(int):
        x = 0
        r = np.random.uniform(0,1,n)
        tr = 1
        for num in r:
            if tr - b > 0:
                x += 1
                tr *= num
        array.append(x)
    graficar_poisson(array, n)
    return array


'''
print(hypergeometricDistribution(100,26,0.5,10))
print (poissonDistribution(5,100,10))
print("Ejemplo de Hipergeometrica (10,5,0.5,100)")
print(hypergeometricDistribution(10,2,10,7))
print("Ejemplo de Binomial (10,0.5,100)")
print(binomialDistribution(10,0.2,7))
'''