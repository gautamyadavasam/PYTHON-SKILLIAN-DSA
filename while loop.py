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


# Q1. Print numbers from 1 to n (increasing order).
# 👉 (Take n as input from the user, use while.)
# n = int (input("eter a postiove integer:- "))
# i =1
# while i<=n:
#     print(i)
#     i+=1


# Q2. Print even numbers from 2 to n.
# 👉 (Hint: you can use n % 2 == 0 to check even numbers.)
# n= int(input("enter a number:- "))
# i=2
# while i<=n:
#     print(i)
#     i+=2

# n= int(input("enter a number:- "))
# i=0
# while i<=n:
#     if i%2==0:
#         print(i)
#     i+=1


# Q3. Print the sum of numbers from 1 to n.
# 👉 (For example, if n = 5, output should be 15 because 1+2+3+4+5=15.)

# n = int(input("Enter a number: "))
# i = 1
# total = 0

# while i <= n:
#     total = total + i   # keep adding i to total
#     i += 1

# print("Sum =", total)


# Q4. Print the multiplication table of a number entered by the user.
# 👉 (For example, if user enters 3, print 3x1=3, 3x2=6, … 3x10=30.)
# n = int(input("write a number- "))
# i =0
# while i <=10:
#     print(n*i)
#     i+=1


# Q5. Reverse a number using while loop.
# 👉 (For example, if user enters 1234, output should be 4321.)
# (Hint: use % 10 and // 10.)
# n = int(input("enter a number:- "))
# rev= 0 
# while n>0:
#     digit=  n%10
#     rev=rev *10 +digit
#     n= n//10
# print("Reverd number=",rev)

# explantaion:- """Start: n = 654321, rev = 0

# Iter 1:
#   digit = 654321 % 10 = 1
#   rev   = 0*10 + 1 = 1
#   n     = 654321 // 10 = 65432

# Iter 2:
#   digit = 65432 % 10 = 2
#   rev   = 1*10 + 2 = 12
#   n     = 65432 // 10 = 6543

# Iter 3:
#   digit = 6543 % 10 = 3
#   rev   = 12*10 + 3 = 123
#   n     = 6543 // 10 = 654

# Iter 4:
#   digit = 654 % 10 = 4
#   rev   = 123*10 + 4 = 1234
#   n     = 654 // 10 = 65

# Iter 5:
#   digit = 65 % 10 = 5
#   rev   = 1234*10 + 5 = 12345
#   n     = 65 // 10 = 6

# Iter 6:
#   digit = 6 % 10 = 6
#   rev   = 12345*10 + 6 = 123456
#   n     = 6 // 10 = 0   → loop stops (n == 0)
# """

# 👉 Check if a number is a palindrome.
# (A palindrome is a number that reads the same forwards and backwards, like 121 or 5445.)                                            
# n= int(input("enter a number:- "))
# original=n 
# rev= 0
# while n>0:
#     num= n%10
#     rev=rev*10+num
#     n=n//10
# if original== rev :
#     print("palindrome")
# else:
#     print("not palindrome")
# print(rev)

# Q6. Find the sum of the digits of a number.
# 👉 Example: if the user enters 1234, the output should be 1+2+3+4 = 10.                                                                                                 
# n = int(input("enter a number:- "))
# store= 0
# while n>0:
#     num= n%10
#     store= store+num
#     n=n//10
# print("sum of the ",n,"is" , store)

#Q8. Count the number of digits in a given number.
# 👉 Example: if the input is 654321, the output should be 6 because it has 6 digits.
# n = int(input("enter a number:- "))
# i= 0 
# while n >0:
#     n=n//10
#     i+=1
# print(i)

# Q7. Find the product of the digits of a number.
# Example:
# If n = 1234, then product = 1 × 2 × 3 × 4 = 24.
# n = int(input("what is the multipliaction of :-  "))
# store= 0
# while n>0:
#     dicr=n%10
#     store=store*dicr
#     n=n//10
# print(store)
#print no from 1 to n take input from the user and dp it using whie loop 
# n = int(input("enter a number :-"))
# a =0
# while a<n:
#     print(a)
#     a+=1

#take a input from the user and print no from n to 0 using while loop 
# n = int(input("enter number "))

# while n>0:
#     print(n)
#     n=n-1

#print all the even number fron 1 to n 
# n= int(input("enter a number :- "))
# a =2
# while a<=n:
#     print(a)
#     a+=2

# n = int(input("enter a number:- "))
# a =1 
# while a<=n:
#     if a%2==0:
#         print(a)
#     a+=1

#lest correct password is "abc" ask  user for the password until he write the right password 
# n =str(input("enter the password:- "))
# while n!="abc":
#     print("retry , wrong password")
#     n =str(input("enter the password:- "))
# print("welcome to the dashboard")


# password = 123   # password is int
# n = int(input("Enter the password: "))

# while n != password:
#     print("Retry, wrong password")
#     n = int(input("Enter the password: "))

# print("Welcome to dashboard")

#Print the sum from 1 to n and take the n from the user 
# n = int (input("enter the number :- "))
# store= 0 
# a=1
# while a<=n:
#     store=store+a
#     a+=1
# print(store)

#prrint all the numbersfrom 1 to n  which was divesable by 5 & 3 
# n =int(input("enter the number :- "))
# a =1
# while a<=n:
#     if a%5==0 and a%3==0:
#         print(a)
#     a+=1

#Write a program that takes the number of rows and columns of a rectangle as input from the user and prints the rectangle.
# from pickletools import int4


# col= 5
# row= 4
# while row>0:
#     temp= col# created a new variable and  when the temp = 0 then the outer loops starts to run and when its fimish to print the coloms its go to printing the rows 
#     while temp>0:# we are giving a condition so tell temps = 0 at till then the loops contniue to run 
#         print("*",end="")# so for not breaing the ;ine we are usng rhe end function so teh star will print in the one line 
#         temp-=1 # this helps to decsing the value of rhe temp  to 5to 4 to 3 to2 to 1 and go on till 0  
#         print()# using for breaking the line so we can print the recentagale by breking the lines 
#     row-=1 #we are dicresing the rows so the rows decsin and the print of redcentagle done succefuly 

# row = 1
# while row <= n:           # outer loop → controls the rows
#     col = 1
#     while col <= c:       # inner loop → controls the columns
#         print("*", end="")   # print stars side by side
#         col += 1
#     print()                  # move to next line after finishing one row
#     row += 1

# #print a square of stars 
# row=int(input("enter a number:"))
# col= row 
# while row>0:
#     temp= col
#     while temp>0:
#         print("*", end="")
#         temp-=1
#     print()
#     row-=1

# print a right angles triangel 
n = 5
row = 1  # start with row 1

while row <= n:  # outer loop → rows
    col = 1      # reset col for each row
    while col <= row:  # inner loop → print stars equal to row number
        print("*", end="")
        col += 1
    print()  # new line after finishing the row
    row += 1  # go to next row


# take string list input from user, and make a new string from them with comma saperated
