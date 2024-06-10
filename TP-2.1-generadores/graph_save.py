import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# Segun https://www.iue.tuwien.ac.at/phd/wasshuber/node46.html 
# x= random_1 y random_n+1
def plot_scatter(leng, seed, list, color=(0, 0, 0), alpha=0.5, title='Scatter plot', xlabel='x', ylabel='y'):
    
    area = np.pi * 3
    # y= list
    # x = np.arange(1, len(y) + 1) 
    x=list
    y = list[1:]+[list[0]] 
    
    
    nombre_archivo = f"plot-{leng}-{str(seed)}.png"

    # Creación del gráfico de dispersión
    plt.scatter(x, y, s=area, c=[color], alpha=alpha)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(f'imagenes_informe\\\\{nombre_archivo}')
    
    plt.show()

def create_bitmap_image(numbers, width, height, output_filename):
    # Crear una nueva imagen en blanco
    im = Image.new("RGB", (width, height), color="black")

    # Asignar cada valor generado a un píxel en la imagen
    pixels = im.load()
    index = 0
    for y in range(height):
        for x in range(width):
            # Escalar el valor para que esté dentro del rango RGB (0-255)
            color_value = int(numbers[index] * 255)
            # Establecer el color del píxel
            pixels[x, y] = (color_value, color_value, color_value)
            index += 1

    # Guardar la imagen como un archivo de imagen
    im.save(output_filename)
    im.show()


def histogram(leng, seed, values):
    # Creas el histograma con intervalos de 0.10
    plt.hist(values, bins=[i/10 for i in range(11)], edgecolor='black')
    nombre_archivo = f"histo-{leng}-{str(seed)}.png"
    plt.savefig(f'imagenes_informe\\\\{nombre_archivo}')

    # Muestras el histograma
    plt.show()