from generadores import GCL_generator, medium_square_generator 
from test import runs_test, frequency_monobit_test, chi_square_test, number_to_bits, generator_to_tests, array_to_string, longest_run_test
from graph_save import plot_scatter, create_bitmap_image, histogram
import random


#SEEDS: 37 // 2500 // 6876 // 7826
seeds=[3700,2500,6876,7826]
s1,s2,s3,s4 = 37,2500,6876,7826
#CANT. NROS: n=10000
n=10000
#PARAMETROS:
#BORLAND C/C++: m=2^32 ; a = 22695477 ; c = 1
#TURBO PASCAL: m=2^32 ; a = 134775813  ; c = 1
#JAVA: m=2^48 - 1 ; a = 25214903917 ; c = 11


#GENERADORES CUADRADOS MEDIOS
#cambiamos el 37 por 3700 ya que debe tener 4 digitos la semilla y 0037 no esta permitido.
gen = 'genSqrMedium'
for s in seeds:
    print('---------------------------------------------------------')
    print('--------------------SEED:', s, '----------------------------')
    print('---------------------------------------------------------')
    list = medium_square_generator(s,n)
    histogram(gen, s, list)
    plot_scatter(gen, s,list, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Generador GCL', xlabel='x', ylabel='y')
    chi_square_test(list, 0.95)
    bits_array = generator_to_tests(list)
    bits_string = array_to_string(bits_array)
    frequency_monobit_test(bits_string)
    print(longest_run_test(bits_array))
    runs_test(bits_string)












"""
#RANDOM
gen = 'random-4'
s=10000
list =[]
for i in range (10000): list.append(random.random())
histogram(gen, s, list)
plot_scatter(gen, s,list, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Generador GCL', xlabel='x', ylabel='y')
chi_square_test(list, 0.95)
bits_array = generator_to_tests(list)
bits_string = array_to_string(bits_array)
frequency_monobit_test(bits_string)
print(longest_run_test(bits_array))
runs_test(bits_string)
"""

"""
#PROBAMOS CON DISTINTOS Ns. USAMOS LOS PARAMETROS DE C
gen = 'genC++'
s= 6876
long=[10,100,1000,10000,100000]
for n in long:
    gen = gen +'-'+ str(n)
    list = GCL_generator(s,22695477,(2**32),1,n)
    histogram(gen, s, list)
    plot_scatter(gen, s,list, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Generador GCL', xlabel='x', ylabel='y')
    chi_square_test(list, 0.95)
    bits_array = generator_to_tests(list)
    bits_string = array_to_string(bits_array)
    frequency_monobit_test(bits_string)
    print(longest_run_test(bits_array))
    runs_test(bits_string)
    gen = 'genC++'

"""



"""
#GENERADOR JAVA
gen = 'genLengJAVA'
for s in seeds:
    print('---------------------------------------------------------')
    print('--------------------SEED:', s, '----------------------------')
    print('---------------------------------------------------------')
    list = GCL_generator(s,25214903917,(2**48 - 1),11,n)
    histogram(gen, s, list)
    plot_scatter(gen, s,list, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Generador GCL', xlabel='x', ylabel='y')
    chi_square_test(list, 0.95)
    bits_array = generator_to_tests(list)
    bits_string = array_to_string(bits_array)
    frequency_monobit_test(bits_string)
    print(longest_run_test(bits_array))
    runs_test(bits_string)

"""



"""
#GENERADOR PASCAL
gen = 'genLengPASCAL'
for s in seeds:
    print('---------------------------------------------------------')
    print('--------------------SEED:', s, '----------------------------')
    print('---------------------------------------------------------')
    list = GCL_generator(s,134775813,(2**32),1,n)
    histogram(gen, s, list)
    plot_scatter(gen, s,list, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Generador GCL', xlabel='x', ylabel='y')
    chi_square_test(list, 0.95)
    bits_array = generator_to_tests(list)
    bits_string = array_to_string(bits_array)
    frequency_monobit_test(bits_string)
    print(longest_run_test(bits_array))
    runs_test(bits_string)

"""



"""
#GENERADOR C++
gen = 'generadorLengC++'
for s in seeds:
    print('---------------------------------------------------------')
    print('--------------------SEED:', s, '----------------------------')
    print('---------------------------------------------------------')
    list = GCL_generator(s,22695477,(2**32),1,n)
    histogram(gen, s, list)
    plot_scatter(gen, s,list, color=(0, 0, 0), alpha=0.5, title='Scatter plot - Generador GCL', xlabel='x', ylabel='y')
    chi_square_test(list, 0.95)
    bits_array = generator_to_tests(list)
    bits_string = array_to_string(bits_array)
    frequency_monobit_test(bits_string)
    print(longest_run_test(bits_array))
    runs_test(bits_string)

"""