"""Given a Book class and a Solution class, write a MyBook class that does the following:

Inherits from Book
Has a parameterized constructor taking these  parameters:
string title
string author
int price
Implements the Book class' abstract display() method so it prints these 3 lines:
Title:, a space, and then the current instance's title.
Author:, a space, and then the current instance's author.
Price:, a space, and then the current instance's proce.
"""

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author

    @abstractmethod
    def display(self):
        pass
    
class MyBook(Book):
    """
    >>> b = MyBook("Dziady", "Adam Mickiewicz", 10)
    >>> b.display()
    Title: Dziady
    Author: Adam Mickiewicz
    Price: 10
    """
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
