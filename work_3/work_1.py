import matplotlib.pyplot as plt

import numpy as np


x = [1, 2, 3, 4, 5, 6, 7]

y = [3.5, 3.8, 4.2, 4.5, 5, 5.5, 7]

fig, (ax, ax1) = plt.subplots(2, 1)

ax.plot(x, y)

ax1.scatter(x, y, c='red', alpha=0.5)

plt.show()