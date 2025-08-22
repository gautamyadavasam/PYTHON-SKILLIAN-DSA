# def count_fact(num):
#     if num==0 or num==1:# base case
#         return 1
#     else:
#         return num* count_fact(num-1)

# print (count_fact(7))


# # This code calculates the factorial of a number using recursion.
# # The function `count_fact` takes a number as input and returns its factorial.
# # The base case is when the number is 0 or 1, in which case it returns 1.
# # Otherwise, it multiplies the number by the factorial of the number minus one.




# # This code is an example of a function that checks if a number is odd or even.
# # It takes an input number and checks if it is divisible by 2.
# # If it is divisible, it prints "even"; otherwise, it prints "odd".
# #write a functon to fin d the factorial of n numbers 
# # def cal_fac(num):
# #     if num/2==0:
# #         print("eve")
# #     else:
# #         print("odd")
# #     cal_fac= (num-1)


# # cal_fac(6)


# list=[1,2,3,4,5,6,7,8,9,]
# student= ["gautam","ram","jado", "madho", "Tony"]

# def p_list(lisss):
#     print(lisss[0])
#     p_list=(lisss(len+1))

# p_list(list)



def print_list_recursive(lst, banana=0):
    if banana == len(lst):
        return
    print(lst[banana])
    print_list_recursive(lst, banana + 1)
