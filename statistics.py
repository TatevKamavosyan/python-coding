# import statistics as stats

# list=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# print("Mean is :", stats.mean(list))
# print("Median is :", stats.median(list))    
# print("Mode is :", stats.mode(list))


# print("Hello, World!")
# name=input("Enter your name: ")  
# # print("Helo"+name+)

# x=5
# y=10.5

# z="Python"
# is_active=True
# print(type(x))
# print(type(y))  
# print(type(z))
# # print(type(is_active))
# a=[7, 11]

# c=[7,11]
# a=c


# print(a is c)  #False
# fruits = ["apple","banana","cherry"]
# print("banana" in fruits) # True
# print("grape" not in fruits) # True

# text = "Hello, world!"
# print("Hello" in text) # True
# # print("bye" not in text) # True

# age = 18
# if age >= 18:
    
#      print("You are eligible to vote.")

# A=40
# B=20
# print(A + B)
# print(A - B)
# print(A * B)
# print(A / B)
# print(A % B)
# print(A ** B)
# print(A // B)

#num=10
# if num >= 1:
#     print("Number is greater than or equal to 1")

# while num > 0:
#     print (num,end="  ")    
#     num-=2

# num=5
# while num!=0:

#     print(num)
#     num-=1

# for i in range(1,6):
    
#         print(i,i)

# rainy = False
# umbrella = True
# if rainy or umbrella:
# print("You are prepared for rain.") # Output: You are prepared for
# rain.
# else:
# print("You might get wet!")
# is_sunny = False
# if not is_sunny:
#     print(is_sunny)

# A=True
# B=False
# print (not B)

# A = [1, 2, 3]
# B = A

# C = [1, 2, 3]
# A= C
# print(A is B) # True (same object)
# print(A is C) # False (different objects with same values)
# print(A is not C) # True (because they are different objects

# AGE=16
# if AGE>= 18:
#     print("You are eligible to vote.")
# else:
#     print("You cant vote yet")    

# marks = 85
# if marks >= 90:
#    print("Grade: A")
# elif marks >= 70 and marks < 90 :
#    print("Grade: B")
# elif marks >= 80:
#    print("Grade: C")
# else:
#    print("Grade: D")

# age = 20
# has_voter_id = True

# if age >= 18 and has_voter_id:
#     print("You are eligible to vote.")          

# else:
#     print("You are not eligible to vote.")
# age = 11
# status = 20 if age >= 18 else "Minor"
# print(status)

# numbers = [1, 2, 3, 4, 5]
# squa)red = list(map(lambda x: x ** 2, numbers))
# print(squared

# student = {"name": "Santhosh", "age": 22, "course": "Python"}
# print(student)
# for num in range(1, 10):
#     if num == 5:
#         break # Stops at 5
# #     print(num)
# for num in range(1, 4):
#    print(num)
# else:
#    print("Loop finished!")
# num = 5
# for i in range(1, 11):
#    print(f"{num} x {i} = {num * i}")


# for i in range(1, 4):
#     for j in range(1, 4):
# #         print(i, j)

# correct_password = "LOOps123"

# write_password= ""
# while write_password != correct_password:
#     write_password=input("Enter the password: ")
#     if write_password == correct_password:
#         print("Access granted.")

# file1= with open("pythonj.py","r")
# # data=file1.read()
# # print(data)
# fruits = ["Apple"
# ,
# "Banana"
# ,
# "Cherry"]
# for i in range(len(fruits)):
#     print(i)

# def power(base, exponent=2): # Default value = 2
#     return base ** exponent

# print(power(3)) # Uses default exponent=2
# print(power(3, 3)) # Overrides default, exponent=3
# def sum_all(*numbers):
#     return sum(numbers)
# print(sum_all(1, 2, 3, 4, 5))

# def greet(name="Guest"):

#     print(f"Hello {name}!")
# greet() # Uses default value
# greet("Chinni")
# def process_data(*args):
#     for item in args:
#         print(f"Մշակվում է {type(item)} տիպի տվյալ")

# process_data([1, 2, 3], {"key": "value"}, (5, 6))

# def logic_1(): return "Արդյունք 1"
# def logic_2(): return "Արդյունք 2"

# def execute_all(*functions):
#     for func in functions:
#         print(func())

# execute_all(logic_1, logic_2)

# def student_info(**kwargs):
#       for key, value in kwargs.items():
#            print(f"{key}: {value}")
# student_info(name="Santhosh"
# , age=21, course="Python")

# def order_summary(order_id,
# *items,
# **details):
#     print(f"Order ID: {order_id}")
#     print("\nItems Ordered:")
#     for item in items:
#         print("-"
# , item)
#     print("\nOrder Details:")
#     for key, value in details.items():
#         print(f"{key}: {value}")
# order_summary(
# 101,
# "Pizza"
# ,
# "Burger"
# ,
# "Coke"
# ,
# name="Santhosh"
# , address="Hyderabad"
# , payment="Online"
# )

# # numbers = [1, 2, 3, 4, 5, 6]
# # evens = list(filter(lambda x: x % 2 == 0, numbers))
# # print(evens)
# import math
# import numpy
# print(dir(numpy))
# # print(dir(math))

# person= 20, 37, 45
# print(person)

# l=5,
# print(l)
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) +1
# print(word_count) # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# data = {"CO2": 400, "O2": 21}

# temp = data.get("temperature", 0)  +1
# print(temp) # Կտպի 0, և ծրագիրը կշարունակի աշխատել:

data = "name:age:location"
print(data.split(":",2)) # Output: ['name', 'age:location']