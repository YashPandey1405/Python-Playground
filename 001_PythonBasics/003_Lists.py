# Lists Are Mutable....

lists=["Yash","Gunnu","Isha",29,31.456,True]

print(lists[0])
print(lists[0:4])
print(lists[0:4:2])
print(lists[-4:-1:2]) 

lists.append("Delhi")
print(lists)

# Lists Methods....
numbers=[3,2,5,4,6,7,8,9,10,1]

'''
numbers.sort()         # Sorts the list in ascending order
numbers.reverse()      # Reverses the list
numbers.append(0)      # Adds 0 to the end of the list
numbers.insert(3, 29)  # Inserts 29 at index 3
numbers.pop(0)         # Removes the first element from the list
numbers.remove(7)      # Removes the first occurrence of 7 from the list
'''