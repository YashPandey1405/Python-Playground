# Dictionaries are mutable & Used To Store Key-Value Pairs....
# Dictionaries are Unordered,Indexed & Can't Contain Duplicate Keys....

marks={
    "Yash" : 90,
    "Divyam" : 96,
    "Shaswat" : 95,
    "Amit" : 100,
    "list" : [90,96,95,100]
}
print(marks,type(marks))
print(marks["list"])

# Dictionary methods and operations in Python.....
my_dict = {
    "name": "Yash", 
    "age": 20, "city": 
    "Mumbai"
}

'''
my_dict.keys()          # Returns a view object of all keys in the dictionary
my_dict.values()        # Returns a view object of all values in the dictionary
my_dict.items()         # Returns a view object of all key-value pairs as tuples
my_dict.get("name")     # Returns the value for the specified key, or None if the key is not found
my_dict.update({"age": 21})  # Updates the dictionary with new key-value pairs
my_dict.pop("city")     # Removes and returns the value of the specified key
my_dict.clear()         # Removes all items from the dictionary
'''