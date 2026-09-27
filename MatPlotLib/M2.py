import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

data = {
    'normal': np.random.normal(0, 1, 1000),
    'uniform': np.random.uniform(-3, 3, 1000),
    'exponential': np.random.exponential(1, 1000)
}

fig, axes = plt.subplots(1, 3, figsize=(10, 8))
i = 0
fig.suptitle('Distributions')
for key, value in data.items():
    axes[i].hist(value, bins=30)
    axes[i].set_title(key)
    axes[i].set_xlabel('value')
    axes[i].set_ylabel('frequency')
    i += 1
plt.tight_layout()
plt.show()