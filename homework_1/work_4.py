# Проверяем коэффициент ковариации


import numpy as np

# создадим массив и транспорируем его, чтобы привести к условию задачи
M0 = np.array([[1, 2, 3, 3, 1],
              [6, 8, 11, 10, 7]])
A = M0.T

mean_a = np.mean(A, axis=0)
print(mean_a)
a_centered = A - mean_a
print(a_centered)

# решение задачи 3
a_centered_sp = np.dot(a_centered[:, 0], a_centered[:, 1])
a_centered_size = a_centered.size
print(a_centered_sp / (a_centered_size - 1))

cov = np.cov(A.T)
print(cov)
