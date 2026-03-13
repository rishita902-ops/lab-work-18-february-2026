import numpy as np

# Create Matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Create Matrix B
B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrix multiplication
result = np.dot(A, B)

print(result)