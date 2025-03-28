"""
NumPy Methods Explanation:
- zeros(): Creates an array filled with zeros.
- ones(): Creates an array filled with ones.
- eye(): Creates an identity matrix.
- empty(): Creates an uninitialized array with random values.
- reshape(): Changes the shape of an array without altering its data.
- @ and np.dot(): Used for matrix multiplication.
- T (Transpose): Transposes rows and columns of a matrix.
- sqrt(): Computes the square root of each element in an array.
- log10(): Computes the base-10 logarithm of each element.
- exp(): Computes the exponential (e^x) of each element.
- min(), max(): Finds the minimum and maximum values in an array.
- np.random(): Generates random numbers.
"""

import numpy as np # type: ignore
print(np.__version__)

# Creating arrays
zero_array = np.zeros((3, 3))
ones_array = np.ones((2, 2))
identity_matrix = np.eye(3)
empty_array = np.empty((2, 3))

# Reshaping an array
reshaped_array = np.arange(6).reshape((2, 3))

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
matmul_1 = A @ B  # Using '@' operator
matmul_2 = np.dot(A, B)  # Using np.dot()

# Transpose
transposed_A = A.T

# Mathematical operations
sqrt_array = np.sqrt(np.array([4, 9, 16]))
log_array = np.log10(np.array([10, 100, 1000]))
exp_array = np.exp(np.array([1, 2, 3]))

# Min and max
random_array = np.random.rand(3, 3)
min_value = random_array.min()
max_value = random_array.max()

# Random number generation
random_numbers = np.random.rand(5)