"""
NumPy Methods and Their Usage:

1. flatten() - Converts a multi-dimensional array into a 1D array.
2. expand_dims() - Expands the dimensions of an array, adding a new axis.
3. squeeze() - Removes single-dimensional entries from an array.
4. repeat() - Repeats elements of an array along a specified axis.
5. roll() - Rolls array elements along a given axis.
6. where() - Returns indices where a condition is met.
7. extract() - Extracts elements from an array based on a condition.
8. byteswap() - Swaps the byte order of the array elements.
9. Operations on NumPy String Array - Various operations like uppercase, lowercase, split, etc.
10. Mathematical Operations in NumPy - Basic arithmetic operations on NumPy arrays.
"""

import numpy as np # type: ignore
print(np.__version__)

# Creating a sample array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 1. flatten()
flat_arr = arr.flatten()
print("Flattened Array:", flat_arr)

# 2. expand_dims()
expanded_arr = np.expand_dims(arr, axis=0)
print("Expanded Array:\n", expanded_arr)

# 3. squeeze()
squeezed_arr = np.squeeze(expanded_arr)
print("Squeezed Array:\n", squeezed_arr)

# 4. repeat()
repeated_arr = np.repeat(arr, 2, axis=1)
print("Repeated Array:\n", repeated_arr)

# 5. roll()
rolled_arr = np.roll(arr, shift=1, axis=1)
print("Rolled Array:\n", rolled_arr)

# 6. where()
condition = arr % 2 == 0
where_result = np.where(condition, "Even", "Odd")
print("Where Condition Result:\n", where_result)

# 7. extract()
extract_result = np.extract(condition, arr)
print("Extracted Even Numbers:", extract_result)

# 8. byteswap()
byte_swapped = arr.astype(np.int16).byteswap()
print("Byte-swapped Array:\n", byte_swapped)

# 9. Operations on NumPy String Array
str_arr = np.array(["hello", "world", "numpy"])
print("Uppercase:", np.char.upper(str_arr))
print("Lowercase:", np.char.lower(str_arr))
print("Title Case:", np.char.title(str_arr))
print("Split Example:", np.char.split(str_arr, "o"))

# 10. Mathematical Operations in NumPy
num_arr = np.array([1, 2, 3, 4])
print("Addition:", num_arr + 10)
print("Subtraction:", num_arr - 2)
print("Multiplication:", num_arr * 3)
print("Division:", num_arr / 2)
print("Exponentiation:", np.exp(num_arr))
print("Square Root:", np.sqrt(num_arr))
