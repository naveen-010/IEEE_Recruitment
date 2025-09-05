import numpy as np

arr = np.random.randint(low = 1, high = 100, size = (5,5))
mean = arr.mean()
maxx = arr.max()
minn = arr.min()

print(arr)  # Grid format print
print("Max: ", maxx , ", Min: ", minn, ", Mean: ", mean)
narr = (arr - minn)/(maxx - minn)


farr = arr.flatten()
print()
print()
print("Flattened array : \n", farr)