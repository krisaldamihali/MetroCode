import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

x = symbols('x')
f = x**2
f_prime = diff(f, x)

f_lamb = lambdify(x, f)
f_prime_lamb = lambdify(x, f_prime)

x_vals = np.linspace(-5, 5, 100)
y_vals = f_lamb(x_vals)

x0 = 2
y0 = f_lamb(x0)
slope = f_prime_lamb(x0)
tangent = slope * (x_vals - x0) + y0

plt.plot(x_vals, y_vals, label='f(x) = x^2')
plt.plot(x_vals, tangent, '--', label='Tangentia në x=2')
plt.scatter(x0, y0, color='red')
plt.legend()
plt.grid(True)
plt.title('Derivati si Tangente')
plt.show()