import math
# Variables
student_count = 1000
rating = 4.99
is_published = False
course_name = "Python"
tree_line = """
multiple
Line
"""
x = 2
y = 1
z = x+y
x, y, z = 2, 1, x+y

print(z)

#  Dynamic Typing

student = 100

print(type(student))

# type annotation

age = 10
age = "ten"

print(age)

# string

a = "faruk"

print(len(a))
print(a[0])
print(a[-2])
print(a[-1])
print(a[0:5])
print(a[:5])
print(a[:])
print(id(a))
print(id(a[0]))

# Escap sequence

message = "programming \'Contest"

print(message)

# format string

first_name = "Omar"
last_name = "Faruk"

full = first_name + " " + last_name

full_name = f"{first_name} {last_name}"
print(full)
print(full_name)

# String Method

course = " Python Programming"

print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find('Pro'))
print(course.replace("P", "-"))
print("Programming" in course)

# Numbers

x = 10
x = 0b10
print(bin(x))

x = 0x12c
print(hex(x))

y = 1 + 2j
print(y)

# Arithmetic Operator
# addition
x = 10 + 3
# subtraction
x = 10 - 3
# multiplication
x = 10 * 3
# division
x = 10 / 3
# without float value
x = 10 // 3
# modulus
x = 10 % 3
# power
x = 10 ** 3

print(x)

# number function
PI = -3.1416
# PI = 1
print(round(PI))
print(abs(PI))
print(math.floor(PI))

# Type Conversion

x = input("x:")

print(int(x))
print(float(x))
print(bool(x))

# falsy
# "", 0, [], None (Null)

# Conditional statment

age = int(input("Enter Your age: "))

if age >= 18:
    print("adult")
elif age >= 13:
    print("Tinezzer")
else:
    print("Child")

print("All are ok")


# Logical Operator
# AND, OR, NOT

name = " "

if not name.strip():
    print("name is Empty")

new_age = 25

if new_age > 20 and new_age < 50:
    print("this age is acceptable")
else:
    print('not acceptable')

color = "rad"

if color == "blue" or color == "green":
    print("color is acceptable")
else:
    print("color is not acceptable")

# Ternary Operator

t_age = 18

message = "acceptable" if age < 15 else "Not acceptable"

print(message)

# For Loop