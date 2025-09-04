# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Alice")
# print(s1.name)

# s2= Student("gautam")
# print()

# Create a Book class with these attributes:

# title

# author

# year

# Add a method show_details() that prints something like:
# "Book: Harry Potter | Author: J.K. Rowling | Year: 1997"

# Create 3 different books (objects) and show their details.
class Book:
    def __init__(self, title, author, year ):
        self.title=title
        self.author=author
        self.year= year

def details(self):
    if self.year<=2000:
        self.year=="old"
    else:
        print("new")
        print(f"Book: {self.title} | Author: {self.author} | Year: {self.year}")
