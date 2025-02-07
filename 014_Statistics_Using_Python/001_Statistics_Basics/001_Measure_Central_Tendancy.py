# Measures Of Central Tendancy....
import numpy as np # type: ignore
import statistics

age=[15,75,29,86,45,58,37,41]

# Mean Calculation Using Numpy.....
print(f"Mean Of {age} Is : {np.mean(age)}")

# Median Calculation Using Numpy.....
print(f"Median Of {age} Is : {np.median(age)}")

# Mode Calculation Using Statistics.....
print(f"Mode Of {age} Is : {statistics.mode(age)}")