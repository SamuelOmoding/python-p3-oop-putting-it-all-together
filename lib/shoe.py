#!/usr/bin/env python3

class Shoe:
    # Defining the constructor method that initializes the Shoe object
    def __init__(self, brand, size):
        # To set the brand attribute to the brand parameter passed to the constructor
        self.brand = brand
        # To set the size attribute to the size parameter passed to the constructor
        self.size = size
        # To set the condition attribute to "Used"
        self.condition = "Used"

    # Defining a property decorator for the size attribute
    @property
    def size(self):
        # To return the value of the private _size attribute
        return self._size

    # Defining a setter method for the size property
    @size.setter
    def size(self, value):
        # To check if the value passed to the setter is an integer
        if isinstance(value, int):
            # To set the private _size attribute to the value passed to the setter
            self._size = value
        else:
            print("size must be an integer")
     # Define a method for the Shoe class that resets the condition attribute to "New"
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
pass
