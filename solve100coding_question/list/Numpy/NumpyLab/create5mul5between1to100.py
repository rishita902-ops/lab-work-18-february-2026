import numpy as np

# Create a 5x5 matrix with random integers from 1 to 100
matrix = np.random.randint(1, 101, (5, 5))

print("Matrix:")
print(matrix)

# Find minimum and maximum values
print("Min =", matrix.min())
print("Max =", matrix.max())