#!/usr/bin/env python

class MyClass1:
    def __init__(self, value):
        self.value = value
        print ("in __init__",hash(self.value))

    def __hash__(self):
        print ("in __hash__",hash(self.value))
        return hash(self.value)

class MyClass2:
    def __init__(self, value):
        self.value = value

print ("\nWith hash")
my_object1 = MyClass1(5) # Creating an object
print( hash(my_object1)) # Print the hash value

print ("\nWithout hash")
my_object2 = MyClass2(5) # Creating an object
print(hash(my_object2))   # Printing the hash value
