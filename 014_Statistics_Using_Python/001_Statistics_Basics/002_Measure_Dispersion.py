import numpy as np # type: ignore
import seaborn as sns # type: ignore
import statistics

Numbers=[2,3,4,5,7,8,9]

# Range
print(f"The Range Will Be : {max(Numbers)-min(Numbers)}")

# Percentile
ans=np.percentile(Numbers,[0,25,50,75,100])
print(f"The Percentile Will Be : {ans}")

# Inter-Quartile Range(ITR) -> Q3 - Q1...
# Lower-Fence -> Q1 - (1.5*IQR)
# Upper-Fence -> Q3 + (1.5*IQR)
print(sns.boxplot(Numbers))

# Variance
print(f"The Variance By Numpy Will Be : {np.var(Numbers)}")
print(f"The Sample-Variance By Statistics Will Be : {statistics.variance(Numbers)}")
print(f"The Public-Variance By Statistics Will Be : {statistics.pvariance(Numbers)}")

# Standard-Deviation
print(f"The Standard-Deviation Will Be : {np.std(Numbers)}")