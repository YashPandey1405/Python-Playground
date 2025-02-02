"""
NumPy Methods Demonstration:
- np.fromfunction(): Creates an array by executing a function over each coordinate.
- np.fromiter(): Creates an array from an iterable.
- np.arange(): Creates an array with a range of values.
- np.fromstring(): Creates an array from a string.
- np.linspace(): Creates an array with evenly spaced values.
- np.logspace(): Creates an array with logarithmically spaced values.
"""

import numpy as np # type: ignore
print(np.__version__)

# np.fromfunction()
def func(x, y):
    return x + y
arr_func = np.fromfunction(func, (3, 3), dtype=int)
print("Array from function:")
print(arr_func)
print("Shape:", arr_func.shape)   # Returns the shape (dimensions) of an array.....
print("Size:", arr_func.size)     # Returns the total number of elements in an array....

# np.fromiter()
iterable = range(5)
arr_iter = np.fromiter(iterable, dtype=int)
print("\nArray from iterable:", arr_iter)

# np.arange()
arr_arange = np.arange(1, 10, 2)
print("\nArray from arange:", arr_arange)

# np.fromstring()
string_data = "1 2 3 4 5"
arr_string = np.fromstring(string_data, dtype=int, sep=' ')
print("\nArray from string:", arr_string)

# np.linspace()
arr_linspace = np.linspace(1, 10, 5)
print("\nArray from linspace:", arr_linspace)

# np.logspace()
arr_logspace = np.logspace(1, 3, 5)
print("\nArray from logspace:", arr_logspace)