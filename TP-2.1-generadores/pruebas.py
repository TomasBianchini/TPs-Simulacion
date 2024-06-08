from generadores import GCL_generator, medium_square_generator 
from test import runs_test, frequency_monobit_test, chi_square_test, number_to_bits
from graph import plot_scatter, create_bitmap_image
from testLongestOnes import longest_run_test
import random


##TEST GENERADORES LGC
#h = GCL_generator(1, 1664525, 2**32 , 1013904223,10)
#print(h)
# h2 = runs_test(h)
# print('Runs Test Linear Congrutial Generator=',h2)
# h3 = frequency_monobit_test(h)
#print('Monibit Test Linear Congrutial Generator=',h3)

""" 
##TEST GENERACION VALORES MEDIOS
h = medium_square_generator(5735, 100)
print(h)
h2 = runs_test(h)
print('Runs Test Middle Square=',h2)
h3 = frequency_monobit_test(h)
print('Monibit Test Middle Square=',h3)
h4 = chi_square_test(h, 10, 0.05)
print('Chi Test Middle Square=',h4)
h5 = []
for i in h:
    h5.extend(number_to_bits(int(i*1000)))
print('Cantidades de unos seguidas:' , longest_run_test(h5))

"""


"""
##TEST GENERACION LGC VS RAMNDOM
h = GCL_generator(500, 106, 6075 , 1283,5000)
plot_scatter(h, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Generador GCL', xlabel='x', ylabel='y')
random_numbers = [random.random() for _ in range(5000)]
plot_scatter(random_numbers, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Random Function', xlabel='x', ylabel='y')
"""

"""ES PROBLEMATICO NO SE EJECUTA
##TEST GENERACION LGC
# Generar números pseudoaleatorios usando tu generador LCG
lcg_numbers = GCL_generator(1, 1664525, 2**32, 1013904223, 512 * 512)
#print(lcg_numbers)
# Crear una imagen de bitmap a partir de los números generados
create_bitmap_image(lcg_numbers, 512, 512, "lcg_bitmap.png")
 """
"""
##TEST GENERACION VALORES MEDIOS
# Generar números pseudoaleatorios usando el método Middle Square
middle_square_numbers = medium_square_generator(8217, 512 * 512)
#print(middle_square_numbers)
# Crear una imagen de bitmap a partir de los números generados
create_bitmap_image(middle_square_numbers, 512, 512, "middle_square_bitmap.png")

"""

"""
###GENERADORES BUENOS
h = GCL_generator(3920, (1+4*9791), 6075 , 1283,5000)
plot_scatter(h, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Generador GCL', xlabel='x', ylabel='y')
print(h)
h2 = runs_test(h)
print('Runs Test Middle Square=',h2)
h3 = frequency_monobit_test(h)
print('Monibit Test Middle Square=',h3)
h4 = chi_square_test(h, 10, 0.05)
print('Chi Test Middle Square=',h4)
h5 = []
for i in h:
    h5.extend(number_to_bits(int(i*1000)))
print('Cantidades de unos seguidas:' , longest_run_test(h5))

"""

##PRUEBA TEST ONES - FUNCIONA CORRECTAMENTE
s = '11001100000101010110110001001100111000000000001001001101010100010001001111010110100000001101011111001100111001101101100010110010'
h = []
for b in s: h.append(int(b))
print(longest_run_test(h))