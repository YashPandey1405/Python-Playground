# Generator function
def my_generator(iterable):
    for item in iterable:
        yield item

# Example with a string
print("String Generator:")
for char in my_generator("Hello"):
    print(char)

# Example with a list
print("\nList Generator:")
for num in my_generator([1, 2, 3, 4, 5]):
    print(num)

# Example with a tuple
print("\nTuple Generator:")
for item in my_generator(('a', 'b', 'c', 'd')):
    print(item)
