from functools import reduce

sum=lambda x,y:x+y
elem=[1,2,3,4,5,6,7]

# print(reduce(lambda x,y:x+y,[1,2,3,4,5,6,7]))  
print(reduce(sum,elem))  