# Tuples Are Immutable....

tuples=("Yash","Gunnu","Isha",29,31.456,True)
print(type(tuples))

print(tuples[0])
print(tuples[0:4])
print(tuples[0:4:2]) 
print(tuples[-4:-1:2]) 

# Tuples Method...
my_tuple = (7, 3, 5, 7, 9, 7)
'''
my_tuple.count(7)        # Counts the occurrences of 7 in the tuple
my_tuple.index(5)        # Returns the index of the first occurrence of 5
len(my_tuple)            # Returns the length of the tuple
sorted(my_tuple)         # Returns a sorted list of the tuple elements
max(my_tuple)            # Returns the maximum value in the tuple
min(my_tuple)            # Returns the minimum value in the tuple
'''