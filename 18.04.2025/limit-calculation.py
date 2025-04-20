import sympy as sp

x = sp.symbols('x')
f = (x**2 - 4)/(x - 2)

limit_result = sp.limit(f, x, 2)
print(limit_result)
