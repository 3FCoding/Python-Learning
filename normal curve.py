import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random numbers from a normal distribution with mean 0 and standard deviation 1
data = np.random.normal(loc=0, scale=1, size=1000)

# Plot the histogram and the theoretical density curve
count, bins, ignored = plt.hist(data, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
print("Bins is", bins)
# Plot the normal distribution curve
from scipy.stats import norm
plt.plot(bins, norm.pdf(bins, 0, 1), linewidth=2, color='red')
plt.title("Normal Distribution (mean=0, std=1)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()