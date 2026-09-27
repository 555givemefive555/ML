import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(x, y1, color='red', linestyle='-', label='sin(x)')
ax.plot(x, y2, color='blue', linestyle='--', label='cos(x)')
ax.set_title('Sin and Cos')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)
plt.show()