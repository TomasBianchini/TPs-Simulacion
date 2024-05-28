import numpy as np
from math import sqrt
from scipy.stats import norm
def RunsTest(numbers: list, alpha: float = .05) -> str:
    media_est = np.mean(numbers)
    sec = [1 if r > media_est else 0 for r in numbers] # 1 si es mayor a la media, 0 si es menor
    c = 0
    for i in range(1, len(sec)-1):
        if sec[i-1] != sec[i]: 
            c += 1
    n_0 = sec.count(0) # Cantidad de 0
    n_1 = sec.count(1) # Cantidad de 1
    nn2 = 2*n_0*n_1 
    n = len(sec)
    mean_c = .5+(nn2/n) # Media
    if n_1 == 0 or n_0 == 0:
        return False
    var_c = (nn2*(nn2-n))/((n**2)*(n-1))
    z = (c-mean_c)/sqrt(var_c)
    return abs(z) < norm.ppf(1-alpha/2)