import math
# Variables

# student_count = 1000
# rating = 4.99
# is_published = False
# course_name = "Python"
# tree_line = """
# multiple
# Line
# """
# x = 2
# y = 1
# z = x+y
# x, y, z = 2, 1, x+y
# print(z)

#  Dynamic Typing

# student = 100
# print(type(student))

# type annotation

# age = 10
# age = "ten"
# print(age)

# string

# a = "faruk"
# print(len(a))
# print(a[0])
# print(a[-2])
# print(a[-1])
# print(a[0:5])
# print(a[:5])
# print(a[:])
# print(id(a))
# print(id(a[0]))

# Escap sequence

# message = "programming \'Contest"
# print(message)

# format string

# first_name = "Omar"
# last_name = "Faruk"
# full = first_name + " " + last_name
# full_name = f"{first_name} {last_name}"
# print(full)
# print(full_name)

# String Method

# course = " Python Programming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.find('Pro'))
# print(course.replace("P", "-"))
# print("Programming" in course)

# Numbers

# x = 10
# x = 0b10
# print(bin(x))
# x = 0x12c
# print(hex(x))
# y = 1 + 2j
# print(y)

# Arithmetic Operator
# addition
# x = 10 + 3
# subtraction
# x = 10 - 3
# multiplication
# x = 10 * 3
# division
# x = 10 / 3
# without float value
# x = 10 // 3
# modulus
# x = 10 % 3
# power
# x = 10 ** 3
# print(x)

# number function

# PI = -3.1416
# PI = 1
# print(round(PI))
# print(abs(PI))
# print(math.floor(PI))

# Type Conversion

# x = input("x:")
# print(int(x))
# print(float(x))
# print(bool(x))
# falsy
# "", 0, [], None (Null)

# Conditional statment

# age = int(input("Enter Your age: "))
# if age >= 18:
#     print("adult")
# elif age >= 13:
#     print("Tinezzer")
# else:
#     print("Child")
# print("All are ok")

# Logical Operator

# AND, OR, NOT
# name = " "
# if not name.strip():
#     print("name is Empty")
# new_age = 25
# if new_age > 20 and new_age < 50:
#     print("this age is acceptable")
# else:
#     print('not acceptable')
# color = "rad"
# if color == "blue" or color == "green":
#     print("color is acceptable")
# else:
#     print("color is not acceptable")

# Ternary Operator

# t_age = 18
# message = "acceptable" if age < 15 else "Not acceptable"
# print(message)

# For Loop

# for x in "Python":
#     print(x)
# for x in ['a', 'b', 'c']:
#     print(x)
# for x in range(0, 10, 2):
#     print(x)
# print(type(range(5)))
# print([1, 2, 3, 4, 5])
# names = ['Talha', 'Tasrif', 'Nasir', 'Faruk']
# for name in names:
#     if name.startswith('Ta'):
#         print("Found")
#         break
# else:
#     print("Not Found")


# while Loop
# guess = 0
# answer = 5
# while answer != guess:
#     guess = int(input("Guess: "))
# else:
#     pass

# function

# def increment(x, y):
#     return (x + y)
# print(increment(10, 20))

# def increments(x: int, y: int = 1) -> tuple:
#     return (x, x+y)

# print(increments(3))

# def multiplication(*list):
#     total = 1
#     for number in list:
#         total *= number
#     return total


# print(multiplication(2, 3, 4, 5))


# def save_user(**user):
#     print(user['username'])


# save_user(id=1, username="faruk", age=23, district="Dhaka")


# scope

# message = "b"


# def greet():
#     global message
#     message = 'a'


# greet()
# print(message)


# esecise

# def fizz_buzz(input):
#     if input == 3:
#         return "Fizz"
#     elif input == 5 :
#         return "Buzz"
#     elif input == 15:
#         return "Fizz Buzz"
#     else:
#         return input
# print(fizz_buzz(15))

# data structure
# 1- Lists

# letters = ["a", "b", "c"]
# matrix = [[1, 2], [3, 4]]
# ones = [1] * 20
# combaind = letters + matrix + ones
# numbers = list(range(20))
# chars = list("Hello World")
# print(len(chars), len(numbers))

# 2- Accessing Items

#  letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters[0:3])
# print(letters[::2])
# numbers = list(range(20))
# print(numbers[::-1])

# 3- List Unpacking

# numbers = [1, 2, 3, 4, 5, 6]
# one = numbers[0]
# one, tow, three, *others, last = numbers
# print(last)

# 4- Looping over Lists

# letters = ["a", "b", "c", "d"]
# for index, letter in enumerate(letters):
#     print(index, letter)

# 5- Adding or Removing Items

# letters = ["a", "b", "c", "d"]
# add
# letters.append("e")
# letters.insert(0, '-')
# print(letters)
# remove
# letters.pop(0)
# letters.remove("b")
# del letters[0:3]
# letters.clear()
# print(letters)

# 6- Finding Items

# letters = ["a", "b", "c", "d"]
# print(letters.count('d'))
# if "d" in letters:
#     print(letters.index("d"))

# 7- Sorting Lists

# numbers = [3, 51, 35, 67, 89]
# numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)

# items = [
#     ('product2', 12),
#     ('product1', 5),
#     ('product4', 19),
#     ('product3', 15),
# ]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)


# 8- Lambda Functions

# items = [
#     ('product2', 12),
#     ('product1', 5),
#     ('product4', 19),
#     ('product3', 15),
# ]

# items.sort(key=lambda item: item[1])

# print(items)

# 9- Map Function

# items = [
#     ('product2', 12),
#     ('product1', 5),
#     ('product4', 19),
#     ('product3', 15),
# ]

# prices = []

# for item in items:
#     prices.append(item[1])

# x = list(map(lambda item: item[1], items))
# for item in x:
#     print(item)

# prices = list(map(lambda item: item[1], items))

# print(prices)

# 10- Filter Function

# items = [
#     ('product2', 12),
#     ('product1', 5),
#     ('product4', 19),
#     ('product3', 15),
# ]

# filtered = list(filter(lambda item: item[1] >= 10, items))

# print(filtered)

# 11- List Comprehensions

# items = [
#     ('product2', 12),
#     ('product1', 5),
#     ('product4', 19),
#     ('product3', 15),
# ]

# # prices = list(map(lambda item: item[1], items))
# prices = [item[1] for item in items]
# print(prices);

# # filtered = list(filter(lambda item: item[1] >= 10, items))
# filtered = [item for item in items if item[1] >= 10]
# print(filtered)

# 12- Zip Function

# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# # [(1, 10), (2, 20), (3, 30)]
# print(list(zip("abc", list1, list2)))

# 13- Stacks

# browsing_session = []

# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# browsing_session.pop()
# print(browsing_session)
# browsing_session.pop()
# print(browsing_session)

# 14- Queues
# from collections import deque

# queue = deque([])

# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# print(queue)
# queue.popleft()
# print(queue)

# 15- Tuples

# point = (1, 2) + (3, 4)
# print(point)

# 16- Swapping Variables

# x = 10
# y = 11

# print("x: ", x)
# print("Y: ", y)

# x , y = y, x

# print("x: ", x)
# print("Y: ", y)

# 17- Arrays
# from array import array

# numbers = array("i", [1, 2, 3])
# numbers.append(4)
# numbers.remove(4)
# numbers[0] = 6
# print(numbers)

# 18- Sets

# numbers = [1, 2, 3]
# first = set(numbers)
# second = {1, 5}

# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# if 1 in first:
#     print('yes')

# 19- Dictionaries

# point = {"x": 1, "y": 2}
# list()
# tuple()
# set()
# point = dict(x=1, y=2)
# point['x'] = 10
# point['z'] = 100
# if "a" in point:
#     print(point["a"])

# print(point.get("a", 0))
# del point["x"]
# print(point)

# # for key in point:
# #     print(key, point[key])

# print(point.items())
# for key, value in point.items():
#     print(key, value)

# 20- Dictionary Comprehensions

# values = {x: x * 2 for x in range(5)}

# print(values)

# 21- Generator Expressions

# from sys import getsizeof

# values = (x * 2 for x in range(100000))
# print("gen:", getsizeof(values))

# values = [x * 2 for x in range(100000)]
# print("List:", getsizeof(values))

# values = (x * 2 for x in range(100000))
# print(len(values))

# 22- Unpacking Operator

# numbers = [1, 2, 3]
# print(*numbers)
# print(1, 2, 3)

# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values)
# first = {"x": 1}
# second = {"x": 10, "y": 20}

# combaind = {**first, **second , "z": 2}

# print(combaind)

# 23- Exercise

# from pprint import pprint
# sentence = "This is a common interview Question"

# char_frequency = {}

# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True)

# pprint(char_frequency_sorted[0])

# 1- Exceptions

# numbers = [1, 2]
# print(numbers[3])
# age = int(input("Your Age:"))

# 2- Handling Exceptions
# try:
#     age = int(input("Your Age:"))
# except ValueError as ex:
#     print("You didn't enter valid age.", ex)
# else:
#     print("No exceptions where thrown")

# 3- Handling Different Exceptions

# try:
#     age = int(input("Your Age:"))
#     age_calculate = 10 / age
# except ValueError as ex:
#     print("You didn't enter valid age.", ex)
# except ZeroDivisionError as ex:
#     print("Invalid age calculation.", ex)
# else:
#     print("No exceptions where thrown")

# 4- Cleaning Up

# try:
#     file = open("app.py")
#     age = int(input("Your Age:"))
#     age_calculate = 10 / age
# except (ValueError, ZeroDivisionError) as ex:
#     print("You didn't enter valid age.", ex)
# else:
#     print("No exceptions where thrown")
# finally:
#     file.close()

# 5- The With Statement

# try:
#     file = open("app.py")
#     age = int(input("Your Age:"))
#     age_calculate = 10 / age
# except (ValueError, ZeroDivisionError) as ex:
#     print("You didn't enter valid age.", ex)
# else:
#     print("No exceptions where thrown")
# finally:
#     file.close()

# 6- Raising Exceptions

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less")
#     return 10/age


# # calculate_xfactor(-1)
# try:
#     calculate_xfactor(-1)
# except ValueError as ex:
#     print(ex)


# 7- Cost of Raising Exceptions
# from timeit import timeit

# code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less")
#     return 10/age


# try:
#     calculate_xfactor(-1)
# except ValueError as ex:
#     pass
# """

# print("First code", timeit(code1, number=10000))

# 1- Classes

# 2- Creating Classes

# class Point:
#     def draw(self):
#         print("draw")


# point = Point()

# print(point.draw())

# print(type(point))
# print(isinstance(point, Point))
# print(isinstance(point, int))

# 3- Constructors

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point({self.x}, {self.y})")


# point = Point(1, 2)
# point.draw()

# 4- Class vs Instance Attributes

# class Point:

#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point({self.x}, {self.y})")

# Point.default_color = "Yellow"

# point = Point(1, 2)
# print(point.default_color)
# print(point.default_color)
# point.draw()

# another = Point(3, 4)
# print(point.default_color)
# print(point.default_color)
# another.draw()

# 5- Class vs Instance Methods

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point({self.x}, {self.y})")


# point = Point.zero()
# point.draw()


# 6- Magic Methods

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self) -> str:
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point({self.x}, {self.y})")


# point = Point(1, 2)
# print(str(point))
# point.draw()

# 7 - Comparing Objects

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# point = Point(1, 2)
# other = Point(10, 20)

# print(point > other)

# 8- Performing Arithmetic Operations

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)


# point = Point(10, 20)
# other = Point(1, 2)

# combaind = point + other

# print(combaind.x, combaind.y)

# 12- Inheritance

# class Animal:

#     def __init__(self) -> None:
#         self.age = 1

#     def eat(self):
#         print("eat")

# # animal: Parent, Base class
# # Mammal: Child, sub class


# class Mammal(Animal):

#     def walk(self):
#         print("walk")


# class Fish(Animal):

#     def swim(self):
#         print("swim")


# m = Fish()
# m.eat()
# print(m.age)

# 13- The Object Class

# 14- Method Overriding

# class Animal:

#     def __init__(self) -> None:
#         self.age = 1

#     def eat(self):
#         print("eat")

# # animal: Parent, Base class
# # Mammal: Child, sub class


# class Mammal(Animal):

#     def __init__(self) -> None:
#         self.weight = 12

#     def walk(self):
#         print("walk")


# class Fish(Animal):

#     def swim(self):
#         print("swim")


# m = Mammal()
# print(m.age)
# print(m.weight)

# 15- Multi-level Inheritance

# class Animal:

#     def eat(self):
#         print("eat")


# class Bird(Animal):

#     def fly(self):
#         print("fly")

# class Chicken(Bird):

#     def ch(self):
#         print("Multilevel")


# c = Chicken()
# c.fly()

# 16- Multiple Inheritance

class Animal:

    def eat(self):
        print("eat")


class Bird:

    def fly(self):
        print("fly")


class Chicken(Animal, Bird):
    pass


c = Chicken()
c.eat()
