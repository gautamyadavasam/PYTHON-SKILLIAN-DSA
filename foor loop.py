# #we need to print  all the numbers in a list 
# heros= ["arjun", "srk", "salman", "rdj"]

# for names in heros:
#     print(heros)


#WPA a program to find a number in the list

nums= (1,2,3,4,5,6,3,7)
x= 56
i= 0
for val in nums:
    if val==x:
        print("found at idx ", i)
    i+=1
    

"""
#explanation:- Sure! Let's go step by step and explain this program in **simple English**, and also why `i = 0` is used.zzzzz

### ✅ What the program does:

This program checks **if a number (`x = 56`) is present in a list (`nums`)**.
If the number is found, it prints **the index (position)** where it was found.

---

### 🧠 Line-by-line Explanation:

```python
nums = (1, 2, 3, 4, 5, 6, 3, 7)
```

This creates a **tuple** called `nums` that holds several numbers.

```python
x = 56
```

This is the number we're **trying to find** in the list.

```python
i = 0
```

We set `i = 0` because we want to keep track of the **index (position)** of each number in the list.
The **first number** is at **index 0**, the second at index 1, and so on.

```python
for val in nums:
```

This means: **Go through each number** (`val`) in the list one by one.

```python
    if val == x:
```

This checks: **Is the current number equal to `x` (56)?**

```python
        print("found at idx ", i)
```

If yes, print the message and show the current index `i`.

```python
    i += 1
```

This means: **Increase `i` by 1**, so the next index is correct.

---

### ❓ Why `i = 0` is necessary:

Python’s `for` loop over a list (or tuple) **doesn’t automatically give the index**.
So if we want to know **at what position** we found the number, we need to **keep count manually** using `i`.

`i = 0` starts the count at the beginning, and `i += 1` moves the count forward as we go through the list.

---

### ℹ️ Final Note:

In this program, `x = 56` is **not in the list**, so it will not print anything.

---

### ✅ If you change it to:

```python
x = 3
```

Then output will be:

```
found at idx  2
found at idx  6
```

Because 3 appears at index 2 and 6 in the list.

---

Let me know if you want me to rewrite this code in an easier or shorter way!
"""

# for el in range(6):#stop Condition is  given here 
#     print(el)
    
#PRACTICE  QUESTIONS
#USING FOR LOOP ANDD RANGE 
#QUESTIONS 1:- PRINT NUMBERS 1 TO 100 
# for el in range(1, 100):
#     print (el )

# #questions2:- print numbers from 100 to 1 
# for num in range(100, 0, -1):
#     print(num)

#print  the multiplication table of number n 
# for el in range(3,30,3):
#     print(el)

#print the factorial of. first n numbers 
# n = int(input("enter a positve integer: "))
# fac=1 
# for el in range(1, n+1):
#     fac *=el
    
# print(fac)

#enumerate function
# heros=["ironman", "spiderman", "batman", "superman"]

# def print_heros(heros):
#     for idx, name in enumerate(heros):
#         print(f"Hero {idx + 1}: {name}")
# print_heros(heros)



#write a loop to print the numbers from 1 to 10 
# for val in range(1, 11):
    # print(val)

#👉 Write a for loop to print all even numbers between 1 and 20.
# for val in range (0, 21, 2):
#     print(val)

#👉 Write a for loop to print the multiplication table of 5 (from 5 × 1 up to 5 × 10).
# for i in range (1, 11):
#     print(5*i)


#Write a for loop to print each character of the word "Hello" on a new line.
# str="Hello"
# for val in str:
#     print(val)# this code print the each word in dffrent section beacuse valis the itreator here snd it iterator ecah word in diffrent line so if you want to print the enitire word the write this at the end  end=""

#sum of 1 to 100
# total= 0 
# for val in range (1, 101):
#     total+=val
# print(total)

#👉 Write a for loop to print the squares of numbers from 1 to 10.
# for val in range(1,11):
#     # print(val*val)

#Write a for loop to print numbers in reverse order from 10 down to 1.
# for val in range(11,0,-1):
#     print(val).      
    
# #another way to do this 
# i =0
# for val in range (11):
#     i+=1
#     print(11-i)

#👉 Write a for loop to count how many vowels are in a given word (for example: "programming").
# word="programming"
# vowels= ["a", "e", "i" ,"o",  "u" ]
# count = 0 
# for val in word:
#     if val in vowels:
#         print("the vowels that is in the word is ", val)
#         count+=1
# print(count)

#👉 Suppose you have a string like "abc123xyz". Write a loop that prints only the digits (1, 2, 3).
# str="abc123xyz"
# find=["1","2","3"]
# count=0 
# for val in str:
#     if val in find :
#         print(val)
#         count+=1
# print(count)


#👉 For example, "I love python programming". Write a loop that counts how many spaces " " are in the sentence.
str="i Love python Programing"


ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJQtx1l1OoJUGu9ycsjHJ6qipZJDlcLWsCjn/BZiIXLP yadavgautam932@gmail.com
