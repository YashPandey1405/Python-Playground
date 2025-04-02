set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

# Union Of 2 Sets -> union = set1 | set2
print("Union of set1 and set2: ", set1.union(set2))

# Intersection of 2 sets -> -> intersection = set1 & set2
print("Intersection of set1 and set2: ", set1.intersection(set2))

# Difference of 2 sets -> diff = set1 - set2
print("Intersection of set1 and set2: ", set1.difference(set2))

# Subset And Superset In Python Sets...
print("Subset of set1 and set2: ", set1.issubset(set2))
print("Superset of set1 and set2: ", set1.issuperset(set2))

# Symmetric Difference Of 2 Sets -> SymmDiff = set1 ^ set2
print("Symmetric Difference of set1 and set2: ", set1.symmetric_difference(set2))