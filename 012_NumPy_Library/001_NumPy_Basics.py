# NumPy Library Was Developed By Travis Olephant In 2000s....

import numpy as np # type: ignore
print(np.__version__)

# Example: Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])  # Same For Tuple As Well....
print(arr.ndim)
# print(arr)

# Creating An 2-d Array....
arr_2d = np.array([[1, 2, 3], [4,5,6],[7,8,9]])
print(arr_2d.ndim)
# print(arr_2d)

# Creating An 3-d Array....
arr_3d = np.array([[[1, 2, 3], [4,5, 6]], [[7, 8, 9], [10, 11,12]]])
print(arr_3d.ndim)
# print(arr_3d)

#Creating An Matrix....
arr_matrix = np.array([[1, 2, 3], [4,5,6],[7,8,9]])
print(arr_matrix.ndim)
# print(arr_matrix)

# Another Way To Create Array Using np.asarray() & np.asanyarray().....
# `np.asarray()` converts input to a NumPy array without making a copy if it's already an array.......
#  while `np.asanyarray()` does the same but preserves subclasses like `np.matrix`.....
l=[1,2,3]
arr=np.asarray(l)
newarr=np.asanyarray(arr)
print(f"Th Dimension Of arr Is : {arr.ndim}") 
print(f"Th Dimension Of newarr Is : {newarr.ndim}") 