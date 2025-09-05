import numpy as np
import matplotlib.pyplot as plt
np.random.seed(10)
data = np.random.normal(size=1000)

# data

x = [i for i in range(1, 1001)]
# x 
plt.scatter(x, data)
plt.xlabel("Index")
plt.ylabel("Random number generated")
plt.title("Normal dist of 1000 random numbers")