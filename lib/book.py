#!/usr/bin/env python3

class Book:
    # Defining the constructor method that initializes the Book object
    def __init__(self, title, page_count):
        # Setting the title attribute to the title parameter passed to the constructor
        self.title = title
        # Calling the private _set_page_count method to set the page_count attribute
        self._set_page_count(page_count)
        # Setting the current_page attribute to 1
        self.current_page = 1

    # Defining a private method for the Book class that sets the page_count attribute
    def _set_page_count(self, value):
        # Checking if the value passed to the method is an integer
        if isinstance(value, int):
            # Setting the page_count attribute to the value passed to the method
            self.page_count = value
        else:
            # Printing an error message if the value passed to the method is not an integer
            print("page_count must be an integer")

    # Defining a method for the Book class that simulates turning a page in the book
    def turn_page(self):
        # Checking if the current_page attribute is less than the page_count attribute
        if self.current_page < self.page_count:
            # Increment the current_page attribute by 1
            self.current_page += 1
            # Printing a message indicating that the page was turned
            print("Flipping the page...wow, you read fast!")
        else:
            # Print a message indicating that the end of the book has been reached
            print("You've reached the end of the book.")   
pass
    
        