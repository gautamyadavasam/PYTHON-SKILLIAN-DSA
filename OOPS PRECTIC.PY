class Student:
    def __init__(self,name,marks,subjects):
        self.name=name
        self.marks=marks
        self.subjects=subjects
        print("welcome to abac college")
        
s1=Student("gautam","56",["maths", "science","english"])
print(s1.name,s1.marks,s1.subjects)

s2=Student("ram","45",("english","hindi","maths"))
print(s2.name,s2.marks,s2.subjects)

s3=Student("shyam","43",("english","hindi","maths"))
print(s3.name,s3.marks,s3.subjects)

def avrage(self):
    return (self.marks + s2.marks + s3.marks) / 3
print(self.avrage)
VVVMVC 