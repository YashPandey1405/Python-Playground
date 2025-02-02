"""
Understanding numpy.matlib:

1. matlib.zeros() - Creates a matrix filled with zeros.
2. matlib.ones() - Creates a matrix filled with ones.
3. matlib.eye() - Creates an identity matrix.
4. matlib.rand() - Generates a matrix with random values.
5. matlib.repmat() - Repeats a matrix multiple times.
6. matlib.empty() - Creates an uninitialized matrix.
7. matlib.identity() - Creates an identity matrix of a given size.
8. Matrix vs. Array - Difference between numpy.matrix and numpy.array.
"""

import numpy as np # type: ignore

# 1. matlib.zeros()
zero_matrix = np.matlib.zeros((3, 3))
print("Zero Matrix:\n", zero_matrix)

# 2. matlib.ones()
ones_matrix = np.matlib.ones((3, 3))
print("Ones Matrix:\n", ones_matrix)

# 3. matlib.eye()
identity_matrix = np.matlib.eye(3, 3)
print("Identity Matrix:\n", identity_matrix)

# 4. matlib.rand()
random_matrix = np.matlib.rand(3, 3)
print("Random Matrix:\n", random_matrix)

# 5. matlib.repmat()
original_matrix = np.matlib.eye(2)
repeated_matrix = np.matlib.repmat(original_matrix, 2, 3)
print("Repeated Matrix:\n", repeated_matrix)

# 6. matlib.empty()
empty_matrix = np.matlib.empty((2, 2))
print("Empty Matrix (Uninitialized Values):\n", empty_matrix)

# 7. matlib.identity()
identity_matrix_2 = np.matlib.identity(4)
print("Identity Matrix of size 4:\n", identity_matrix_2)

# 8. Matrix vs. Array
matrix_example = np.matlib.matrix([[1, 2], [3, 4]])  # Creates a matrix
array_example = np.array([[1, 2], [3, 4]])          # Creates a NumPy array

print("Matrix Example:\n", matrix_example)
print("Array Example:\n", array_example)

# Checking the type
print("Type of matrix_example:", type(matrix_example))
print("Type of array_example:", type(array_example))

# Matrix multiplication behavior
print("Matrix Multiplication (matlib matrix * matlib matrix):\n", matrix_example * matrix_example)  # Works as expected
print("Array Multiplication (NumPy array * NumPy array):\n", array_example * array_example)  # Element-wise multiplication

# Converting a matrix to an array
converted_array = np.asarray(matrix_example)
print("Converted Matrix to Array:\n", converted_array)

