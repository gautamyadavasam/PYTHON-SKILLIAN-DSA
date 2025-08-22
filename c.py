# i=int(input(" enter number"))
# if i in range(10,25,):
#     print(i,"its there")
# else:
#     print("not there")





# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     grade = "A"
# elif marks >= 75:
#     grade = "B"
# else:
#     grade = "C"

# print("Your grade is:", grade)















# radius =  int (input("Enter the radius of the circle: "))
# area = 3.14* radius * radius
# print("The area of the circle is:", area)














a = float(input("Enter the frist side: "))
b = float(input("Enter the 2nd side: "))
c = float(input("Enter the 3rd  side: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")



