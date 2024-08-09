import sys
from multipleRunings import *
from oneRuning import *

def parse_arguments():
    if len(sys.argv) != 4:
        print("Uso: python script.py <mean_service> <mean_interarrival> <multiple_runs>")
        sys.exit(1)
    
    try:
        mean_service = float(sys.argv[1])
        mean_interarrival = float(sys.argv[2])
        multiple_runs = int(sys.argv[3])
    except ValueError:
        print("Error: Por favor ingrese valores correctos.")
        sys.exit(1)
    
    return mean_service, mean_interarrival, multiple_runs

def ask_for_infinite_queue():
    response = input("¿Cola Infinita? [Y/N]: ").strip().upper()
    if response == 'Y':
        return True
    elif response == 'N':
        return False
    else:
        print("Respuesta no válida. Debe ingresar 'Y' o 'N'.")
        return ask_for_infinite_queue()

if __name__ == "__main__":
    mean_service, mean_interarrival, multiple_runs = parse_arguments()
    if multiple_runs == 1:
        oneRuningProgram(mean_interarrival, mean_service)
    else:
        infinite_queue = ask_for_infinite_queue()
        multiple_runings_program(mean_interarrival, mean_service, infinite_queue)
