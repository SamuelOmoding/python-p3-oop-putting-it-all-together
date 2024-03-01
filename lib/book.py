#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._set_page_count(page_count)
        self.current_page = 1

    def _set_page_count(self, value):
        if isinstance(value, int):
            self.page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print("Flipping the page...wow, you read fast!")
        else:
            print("You've reached the end of the book.")
    pass
    
        