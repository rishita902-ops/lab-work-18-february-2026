import numpy as np

# Generate 10 random numbers between 0 and 1
arr = np.random.rand(10)

print("Original Array:")
print(arr)

# Min-max normalization
normalized_arr = (arr - arr.min()) / (arr.max() - arr.min())

print("Normalized Array:")
print(normalized_arr)