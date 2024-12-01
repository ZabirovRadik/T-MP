import numpy as np
import math
import matplotlib.pyplot as plt

from scipy.integrate import quad
from scipy.optimize import fsolve

# 1.

matrix_10x10 = np.ones((10, 10), dtype = float)
identity_matrix_10x10 = np.eye(10)

print("Матрица 10x10 из вещественных единиц:")
print(matrix_10x10)
print("\nЕдиничная матрица 10x10:")
print(identity_matrix_10x10)

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
    integral_2, error = quad(lambda x: np.cos(2 * x), 0, np.inf)
    print("\nРезультат интеграла 1:")
    print(integral_1)

    print("\nРезультат интеграла 2:")
    print(integral_2)
    print(f"Ошибка оценки: {error}")
    print(f"Это произошло так как интеграл расходится")
    return (integral_1, integral_1)



# 5. Построение графиков функций
x = np.linspace(-10, 10, 400)
y1 = np.sin(x + np.pi / 3)
y2 = 2 * x

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y = sin(x + π/3)', color='blue')
plt.plot(x, y2, label='y = 2x', color='red')
plt.title('Графики функций')
plt.xlabel('x')
plt.ylabel('y')
idx = np.argwhere(np.diff(np.sign(y1 - y2))).flatten()
plt.plot(x[idx], y1[idx], 'ro')
plt.legend()
plt.grid()
plt.show()