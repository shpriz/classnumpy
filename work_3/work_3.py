import numpy as np
import matplotlib.pyplot as plt


N = 51

x = np.linspace(-3, 3, N, endpoint=True)

y1 = [i**2 for i in range(len(x))]
y2 = [2*i + 0.5 for i in range(len(x))]
y3 = [-3 * i - 1.5 for i in range(len(x))]
y4 = [np.sin(i) for i in range(len(x))]

plt.figure(figsize=[8, 6])
plt.subplots_adjust(wspace=0.3, hspace=0.3)

plt.subplot(221)
plt.plot(x, y1, '-r', linewidth=4)
plt.title('График y1')
plt.xlabel('Значения x')
plt.ylabel('Значения y1')
plt.axis([-5, 5, -100, 2600])



plt.subplot(222)
plt.plot(x, y2, '-b', linewidth=4)
plt.title('График y2')
plt.xlabel('Значения x')
plt.ylabel('Значения y2')

plt.subplot(223)
plt.plot(x, y3, linewidth=4)
plt.title('График y3')
plt.xlabel('Значения x')
plt.ylabel('Значения y3')

plt.subplot(224)
plt.plot(x, y4, '-b', linewidth=4)
plt.title('График y4')
plt.xlabel('Значения x')
plt.ylabel('Значения y4')

plt.show()
