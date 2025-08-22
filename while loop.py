# # # # # # # A example of a normal loop 

# # # i= 1
# # # while i<=5:
# # #     print("helo")
# # #     i+=1

# # # # # #WAp to print a number 1 to 100 

# # # # # # i = 1
# # # # # # while i<=100: #the line written after the while is known as stoping Condition this helps to stop the loop and its very important coz if it is not there then it will create a infinite loop 
# # # # # #     print(i)
# # # # # #     i+=1

# # # # # # print("loop ended")

# # # # # # # WPA to print a table multiplication of number N
# # # # # # num = 5 
# # # # # # i =1
# # # # # # while i<=10:
# # # # # #     print(num*i)
# # # # # #     i +=1








# # # # # # gautam = 1
# # # # # # while gautam  <=1000:
# # # # # #     print("gautam is a software enginer in google" , gautam)
# # # # # #     gautam -=1
# # # # # # print("programe band ho gaya ha bhai")

# # # # # # WPA to Print the numbers from 100 to 1

# # # # # # i =100
# # # # # # while i >=1:
# # # # # #     print("here is the number" , i)
# # # # # #     i-= 1

# # # # # # #WPA to print the multiplication atable of number 3 

# # # # # # num= 1
# # # # # # while num <=10:
# # # # # #     print(3 * num)
# # # # # #     num +=1


# # # # # #WAP to print the element of the following list using loop 

# # # # # list = [20,30, 40,50,60]
# # # # # while idx == max:
# # # # #     print(idx)

# # # # #wapto serch for a number x in this tupple using loop
# # # # list =(23, 45,36,54,78,89,36)
# # # # i= 0
# # # # while i<len(list):
# # # #     if list[i]==36:
# # # #         print("fond at idx",i)
# # # #     else:
# # # #         print("finding ")        
# # # #     i+=1
# # # # print(type(list)) 

# # # # #PRINT ALL THE NAMES BELOW IN THE TUPPLE USING WHILE LOOP 
# # # # Names =("ram", "shyam", "gautam")
# # # # i=0 
# # # # while i< len(Names):
# # # #     print(Names[i])
# # # #     i+=1

# # # #practice questions
# # # #Question1 :- WAP to find the su of first  n natural numbers 
# # # num = int(input("enter the number:  "))
# # # sum= 0
# # # i=1
# # # while i<=num:
# # #     sum +=i
# # #     i+=1
# # # print("the sum of the first ",num , "natural number is ", sum)  



# # #check if a number is in between 1 and 90 without using any logical operator
# # a = int(input("enter a number "))
# # i= 1
# # while i <=90:
# #     i+=1
# # print("this no is true")

# # skillans class 


# #print numbers from 1 to n , take n from user as integaer input

# # n = int(input("enter a postive number:-  "))
# # i =1
# # while i<= n:
# #     print(i)
# #     i += 1
    
# #print numbers from n to 0 (Decreasing order) , take n from user as integaer input

# # n = int(input("Enter a number: "))


# # while n >= 0:
# #     print(n)
# #     n -= 1  

# #print the sum of integers 1 to n 
# # 

# n = int(input("Enter a positive integer: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1      
# print("The sum of integers from 1 to", n, "is:", sum)



#Write a loop that prints numbers from 0 to 4. using the less then Condition 
# i = 0 
# while i<=4:
#     print(i)
#     i+=1

#Write a loop that prints numbers from 10 to 1, going down, using:
# i= 10
# while i >=1:
#     print(i)
#     i-=1
#Write a loop that prints only even numbers from 20 to 2 (counting down).
# i = 20 
# while i>=2:
#     print(i)
#     i-=2  
# 



#Challenge 1 – Mixed Condition

#Print numbers from 5 to 15, but stop the loop if the number is divisible by 7.
#(Hint: use while and % operator)
# i=5
# while i<=15:
#     if i%7==0:
#         break
#     print(i)
#     i+=1 #DOUT WHAT IF WEE WANT TO CONTINUE THE PRIN TO THOES NUMBERS WHICH IS NOT DIVIAVBLE BY 7 
# Challenge 2 – Reverse Odd Numbers

# Print all odd numbers from 15 down to 1.
# (Hint: start from 15, use i -= 2)

# I= 15
# while I>=1:
#     print (I)
#     I-=2

# i= 1
# while i<=20:
#     if i%3==0:
#         continue
#     print(i)
#     i+=1


#print all the numbers from 1 to n which are divisible by 5 and 3
# n  = int(input("Enter a positive integer: "))
# i=-1
# while i<=n:
#     if n % 3 == 0 and  n % 5 == 0:
#         print(n)
#     n -= 1


# row= 4
# colom= 5
# while row=>0:
# #     while colom=>0:
        
# # take rows and columns from user
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# # empty matrix
# matrix = []

# print("Enter elements of the matrix:")

# # Take input for rows and columns
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []
# i = 0

# print("Enter elements row by row:")

# # Outer while loop for rows
# while i < rows:
#     row = []
#     j = 0
#     # Inner while loop for columns
#     while j < cols:
#         element = int(input(f"Enter element at position ({i+1},{j+1}): "))
#         row.append(element)
#         j += 1
#     matrix.append(row)
#     i += 1

# # Printing the matrix nicely
# print("\nMatrix:")
# i = 0
# while i < rows:
#     j = 0
#     while j < cols:
#         print(matrix[i][j], end=" ")
#         j += 1
#     print()  # new line after each row
#     i += 1


# number of rows
rows = 5

i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end="")   
        j = j + 1
    print()  
    i = i + 1
