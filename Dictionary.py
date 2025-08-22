#exaple of a dictonary
student = { #this is the main Dictionary
    "name" : "gautam",
    "class" : "master",
    "marks" : {  # where the subject and the marks are there this is a nested dictionary 
        "phy":45,
        "chem":67,
        "math":67
            }
}
print(student)
print(type(student))
print(len(student))  # this will give the length of the main dictionary
print(student.keys()) # this will give the keys of the main dictionary
print(student.values()) # this will show the vales of all the keys in the dictionary.
print(student.items()) #this will give the key:values of the dictionary in the key and vales pairs  