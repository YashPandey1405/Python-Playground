# Parent class
class Animal:
    def speak(self):
        print("This animal makes a sound.")

# Child class overriding the 'speak' method
class Dog(Animal):
    def speak(self):
        print("The dog barks.")

# Child class overriding the 'speak' method
class Cat(Animal):
    def speak(self):
        print("The cat meows.")

# Creating objects
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the 'speak' method
animal.speak()  # Output: This animal makes a sound.
dog.speak()     # Output: The dog barks.
cat.speak()     # Output: The cat meows.
