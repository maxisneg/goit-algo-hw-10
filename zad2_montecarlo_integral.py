
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція
def f(x):
    return x ** 2

a, b = 0, 2
N = 100000
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
monte_carlo_integral = (b - a) * np.mean(y_random)

# Точний інтеграл через quad
exact_integral, error = quad(f, a, b)

# Вивід
print(f"Інтеграл (Монте-Карло): {monte_carlo_integral}")
print(f"Інтеграл (quad): {exact_integral}, похибка: {error}")

# Графік
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік f(x) = x^2, інтеграл = {monte_carlo_integral:.4f}')
plt.grid()
plt.show()
