import matplotlib.pyplot as plt
import numpy as np

# Generate random data for the histogram
data = np.random.randn(10000)

vals, x_distribution, y_distribution = np.histogram2d(data, data, bins=4, density=True)
res = np.matmul(x_distribution.reshape(-1, 1), y_distribution.reshape(1, -1))
res = res ** -1
print(res, res.sum())

data_ = data.reshape(1, -1)
res = np.matmul(data_.T, data_)

print(res.shape)

# Plotting a basic histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

plt.show()
