#questions:- Create a new file and write some text in it, then read the file and print its content.
# Answer:
# with open ("demo.txt", "w+") as f:
#     f.write("hi everyone \n we are learning file/io \n using python \n i like programing in python ")
#     data =f.read()
#     print(data)
#in this above code the data was not  printed and this is because:- """When you open a file in "w+" mode, the file pointer starts at the beginning, but after writing, it moves to the end of the file. So when you immediately call f.read(), Python tries to read from the end, and that gives you an empty string.""""



#search a word in a file and print if it is found or not.
# word= "am"
# with open("demo.txt", "r") as f:
#     data =f.read()
#     if(data.find(word)!=-1):
#         print("found")
#     else:
#         print("not found ")




#write a function that takes a word as input and checks if it is present in the file or not.
# def check_word():
#     word = input("Enter the word you want to find: ")
#     with open("demo.txt", "r") as f:
#         data = f.read()
#         if (data.find(word)!=-1):
#             print("found")
#         else:
#             print("not found")

# check_word()



#Qyuestion:- search a word in a file and print the line number if it is found.
# word="python "
# data=-1
# line= 1

# with open("demo.txt","r")as f:
#     while data:
#         data= f.readline()
#         if word in data:
#             print("found")
#         else:
#             print("not found ")
            
#             line+=1
        
        
#Question:- search a word in a file and print the line number if it is found.
# word = "python"
# line = 1

# with open("demo.txt", "r") as f:
#     data = f.readline()
#     while data:
#         if word in data:
#             print("found in line", line)
#         line += 1
#         data = f.readline()
#     else:
#         print("not found")



# #Questions:- From a file containinf numbers separated by commas, & print the count of even no 
# count = 0
# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# numbers = data.split(",")   # split the file content into a list

# for val in numbers:
#     if int(val) % 2 == 0:   # check each number # type caste the numbers to int from string 
#         count += 1

# print("count of even numbers is:", count)

# with open("student.txt","w") as f:
#     f.write("gautam yadav\n suraj yadav\n sumit rai")
    
# with open ("student.txt","r")as l:
#     data=l.read()
#     # print(data )

# with open("student.txt","r")as l:
#     line1= l.readlines()
#     print(line1)
#     data=len(line1)
#     print(data)
    

# Create a file and write "Hello, World!" in it. Then read and print it.
# with open("file.txt","w+")as l:
#     l.write("hello World")
# with open("file.txt","r")as l:
#     data=l.read()
#     print(data)


# Write 5 student names in a file (one per line). Read and print each name.
# with open ("file.txt","a+")as f:
#     f.write("\ngautamyadav\nsuraj\nsumit")
#     f.seek(0)
#     data=f.read()
#     print(data)
# Count how many characters are in a file.
# count= 0 
# with open("file.txt","r")as f:
#     data= f.read()
#     for val in data:
#         print(val)
#         count+=1
# print(count)
# # there is a anoter way to do this and hat is the coreect way to do this  
# with open("file.txt","r")as f:
#     data=f.read()
#     print(len(data) )
# # Count how many lines are in a file.
# with open("file.txt","r")as f:
#     data=f.readline()
#     print(len(data))
# Count how many words are in a file.

with open("file.txt","r")as f:
    data=f.read()
    print(data)
    num=data.split()
    print(len(num))
        