# create a student class that takes the names and marks of three student is arguments in constructor, then create a matter to print the average
class Student:
    def __init__(self, name, marks ):
        self.name = name
        self.marks= marks
    def average(self):
        avg =sum(self.marks)/len(self.marks)
        print(f"{self.name}'s average marks are:  {avg}")



#create 3 Students
s1 = Student("Alice",[80,90,70])
s2 = Student("Bob",[60,89,56])
s3 = Student("Charlie", [88,92,78])

s1.average()
s2.average()
s3.average()





# Create a Book class with these attributes:

# title

# author

# year

# Add a method show_details() that prints something like:
# "Book: Harry Potter | Author: J.K. Rowling | Year: 1997"

# Create 3 different books (objects) and show their details.
# class Book:
#     def __init__(self, title, author, year ):
#         self.title=title
#         self.author=author
#         self.year= year

# def details(self):
#     if self.year<=2000:
#         self.year=="old"
#     else:
#         print("new")
#         print(f"Book: {self.title} | Author: {self.author} | Year: {self.year}")
