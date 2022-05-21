import numpy as np
import matplotlib.pyplot as plt


N = 51

x = np.linspace(0, 10, N, endpoint=True)

y = [np.cos(i) for i in range(len(x))]

plt.title('График f(t)')
plt.xlabel('Значения t')
plt.ylabel('Значения f')
plt.axis([0.5, 9.5, -2.5, 2.5])

plt.plot(x, y, '-g')
plt.show()





