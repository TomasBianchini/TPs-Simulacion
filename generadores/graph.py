import numpy as np
import matplotlib.pyplot as plt
# Segun https://www.iue.tuwien.ac.at/phd/wasshuber/node46.html 
# x= random_1 y random_n+1
def plot_scatter(x, y, color=(0, 0, 0), alpha=0.5, title='Scatter plot', xlabel='x', ylabel='y'):
    """
    Genera un gráfico de dispersión con los puntos dados en x e y.

    Parámetros:
    - x: Lista o array de coordenadas x.
    - y: Lista o array de coordenadas y.
    - color: Color de los puntos.
    - alpha: Transparencia de los puntos.
    - title: Título del gráfico.
    - xlabel: Etiqueta del eje x.
    - ylabel: Etiqueta del eje y.
    """
    area = np.pi * 3

    # Creación del gráfico de dispersión
    plt.scatter(x, y, s=area, c=[color], alpha=alpha)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Generación de datos
N = 500
x = np.random.rand(N)
y = np.random.rand(N)

# Llamada a la función con las listas x e y
plot_scatter(x, y)
