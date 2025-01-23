# Iterator on a string
string = "Hello"
string_iter = iter(string)
print("String Iterator:")
for _ in range(len(string)):
    print(next(string_iter))

# Iterator on a list
my_list = [1, 2, 3, 4, 5]
list_iter = iter(my_list)
print("\nList Iterator:")
for _ in range(len(my_list)):
    print(next(list_iter))

# Iterator on a tuple
my_tuple = ('a', 'b', 'c', 'd')
tuple_iter = iter(my_tuple)
print("\nTuple Iterator:")
for _ in range(len(my_tuple)):
    print(next(tuple_iter))
