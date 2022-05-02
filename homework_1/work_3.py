# Найдите скалярное произведение столбцов массива a_centered.
# В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1,
# где N - число наблюдений.


import numpy as np

# создадим массив и транспорируем его, чтобы привести к условию задачи
M0 = np.array([[1, 2, 3, 3, 1],
              [6, 8, 11, 10, 7]])
A = M0.T
# выводим на экран
print(M0)
print(A)
mean_a = np.mean(A, axis=0)
print(mean_a)
a_centered = A - mean_a
print(a_centered)

# решение задачи 3
a_centered_sp = np.dot(a_centered[:, 0], a_centered[:, 1])
a_centered_size = a_centered.size
print(a_centered_sp / a_centered_size)
