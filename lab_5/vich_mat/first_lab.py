import numpy as np
import math
import matplotlib.pyplot as plt

from scipy.integrate import quad
from scipy.optimize import fsolve

# 2.
def first_func(matrix):
    det_result = np.linalg.det(matrix)
    return det_result


# 3. 

def rand_matrix(shape):
    A = np.random.randint(-3, 6, (shape, shape))  
    B = np.random.randint(-3, 6, (shape, 1)) 
    X = np.linalg.solve(A, B)
    return (A, B, X)


# 4. Вычисление интегралов
def find_integral():
    integral_1, _ = quad(lambda x: ((math.exp(3*x) + math.exp(-3 * x)) / 2)**2 , 0, 1 / 3)
    return integral_1