import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma

def relative(X):
    unique, counts = np.unique(X, return_counts=True)
    relative_freq = counts / len(X)
    plt.scatter(unique, relative_freq, color='r')
    plt.plot(unique, relative_freq, linestyle='-', color='r')
    plt.title('Frecuencia Relativa de la Distribución Uniforme')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia Relativa')
    plt.grid(True)
    plt.show()

def grafica(r,x):
        plt.plot(r, x, marker='o', linestyle='none', color='b')
        plt.title('Gráfica de la Exponencial')
        plt.xlabel('Secuencia')
        plt.ylabel('Valores de la Exponencial')
        plt.grid(True)
        plt.show()


def grafica_gamma(array, k, a):
    # Calcular el rango de valores
    xmin, xmax = min(array), max(array)
    x = np.linspace(xmin, xmax, 1000)
    
    # Calcular la densidad de probabilidad usando scipy.stats.gamma
    y = gamma.pdf(x, k, scale=1/a)
    
    plt.plot(x, y, 'r-', lw=2)
    plt.xlabel('Valor')
    plt.ylabel('Densidad de Probabilidad')
    plt.title('Curva de Densidad de la Distribución Gamma')
    plt.show()

def grafica_normal(array, mu, sigma):
    array = np.array(array)
    array.sort()
    density = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(array - mu)**2 / (2 * sigma**2))
    plt.plot(array, density)
    plt.title('Distribución Normal')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de Probabilidad')
    plt.grid(True)
    plt.show()

def graficar_pascal(data, n):
    plt.hist(data, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')
    plt.title('Histograma de la Distribución de Pascal')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de Probabilidad')
    plt.grid(True)
    plt.show()

def graficar_binomial(data,n):
    plt.hist(data, bins=np.arange(n+1)-0.5, density=True, alpha=0.6, color='b', edgecolor='black')
    plt.title('Histograma de la Distribución Binomial')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de Probabilidad')
    plt.grid(True)
    plt.show()

def graficar_hypergeometric(data, ns):
    plt.hist(data, bins=np.arange(ns + 2) - 0.5, density=True, alpha=0.6, color='r', edgecolor='black')
    plt.title('Histograma de la Distribución Hipergeométrica')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de Probabilidad')
    plt.grid(True)
    plt.show()

def graficar_poisson(data, n):
    plt.hist(data, bins=np.arange(n + 2) - 0.5, density=True, alpha=0.6, color='m', edgecolor='black')
    plt.title('Histograma de la Distribución de Poisson')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de Probabilidad')
    plt.grid(True)
    plt.show()