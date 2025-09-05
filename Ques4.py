sliced_arr = arr[1:-1, 1:-1]
print(sliced_arr)

frow = sliced_arr[0]
lcol = sliced_arr.T[-1]

print()
print("First row: ", frow, ", Last col : ", lcol)
print("Dot: ", np.dot(frow, lcol))