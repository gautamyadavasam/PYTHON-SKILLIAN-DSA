# def calssun(a, b ):
#     sum=a+b
#     print(sum)
#     return sum

# calssun(10, 5)


# def calsum(a, b):
#     return a+b

# calsum(5,6)
# print(calsum)


#wap to calclate the average of 3 numbers 
# def average(a,b,c):
#     return (a+b+c) /3

# total= average(1,2,3)
# print(total)

#another Way to do this 
# def cal_avg(a, b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg

# cal_avg(2,5,9)

# #default parameter example 
# def def_par(a=0,b=0):#gere b=1 is the default parameter 
#     sum=a+b
#     print(sum)
#     return sum 

# def_par(1,3)
# if def_par == 0:
#     print("Devloper forget to give the parameters")
# else:
#     print("nice man


#writw a function to find the sqaure  of n number 

# def cal_square (a):
    
#     square= a*a
#     print(square)


# cal_square(6)zzz


#calculate tzzhe faczzztoriial of number n and where n is the parameter 

def cal_fac (n):
    i= 0
    while n==0:
        print(n+i)
        i-=1

cal_fac (6)


#write a funtion to convert the usd to inr 

# def cal_inr(usd):
#     inr = usd*83
#     print(inr)
#     return inr

# cal_inr(1000)


#Waf to take input from the useer anand return the  input in odd or even 

def Check_odd_even(number):
    if input%2==0:
        print("even")
    else:
        print("odd")
        
input= int(input("enter a number"))
Check_odd_even(input)                                       