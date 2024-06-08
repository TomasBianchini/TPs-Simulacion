from generadores import generatorLGC, AlgorithmMiddleSquare 
from test import medianTest, monobit_test, chi_test, number_to_bits
from graph import plot_scatter, create_bitmap_image
from testLongestOnes import longest_run_test
import random


##TEST GENERADORES LGC
#h = generatorLGC(1, 1664525, 2**32 , 1013904223,10)
#print(h)
# h2 = medianTest(h)
# print('Runs Test Linear Congrutial Generator=',h2)
# h3 = monobit_test(h)
#print('Monibit Test Linear Congrutial Generator=',h3)


##TEST GENERACION VALORES MEDIOS
h = AlgorithmMiddleSquare(5735, 100)
print(h)
h2 = medianTest(h)
print('Runs Test Middle Square=',h2)
h3 = monobit_test(h)
print('Monibit Test Middle Square=',h3)
h4 = chi_test(h, 10, 0.05)
print('Chi Test Middle Square=',h4)
h5 = []
for i in h:
    h5.extend(number_to_bits(int(i*1000)))
print('Cantidades de unos seguidas:' , longest_run_test(h5))

""" 
##TEST GENERACION LGC VS RAMNDOM
h = generatorLGC(500, 106, 6075 , 1283,5000)
plot_scatter(h, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Generador GCL', xlabel='x', ylabel='y')
random_numbers = [random.random() for _ in range(5000)]
plot_scatter(random_numbers, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Random Function', xlabel='x', ylabel='y')


##TEST GENERACION LGC
# Generar números pseudoaleatorios usando tu generador LCG
lcg_numbers = generatorLGC(1, 1664525, 2**32, 1013904223, 512 * 512)
#print(lcg_numbers)
# Crear una imagen de bitmap a partir de los números generados
create_bitmap_image(lcg_numbers, 512, 512, "lcg_bitmap.png")


##TEST GENERACION VALORES MEDIOS
# Generar números pseudoaleatorios usando el método Middle Square
middle_square_numbers = AlgorithmMiddleSquare(8217, 512 * 512)
#print(middle_square_numbers)
# Crear una imagen de bitmap a partir de los números generados
create_bitmap_image(middle_square_numbers, 512, 512, "middle_square_bitmap.png")
 """