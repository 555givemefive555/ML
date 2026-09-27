import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 200
X = np.random.randn(n, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlabel('feature 1')
ax.set_ylabel('feature 2')
ax.set_title('Scatter: two classes')
ax.scatter(X[y==0, 0], X[y==0, 1], color='blue', alpha=0.6, s= 50, label='class 0')
ax.scatter(X[y==1, 0], X[y==1, 1], color='red', alpha=0.6, s= 50, label='class 1')
plt.legend()
plt.show()