import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1.5, 2.5, 100)
y = (x**2 - 4)/(x - 2)

plt.plot(x, y, label='f(x)')
plt.axvline(2, color='red', linestyle='--', label='x=2')
plt.legend()
plt.title('Limiti afër x = 2')
plt.grid(True)
plt.show()
