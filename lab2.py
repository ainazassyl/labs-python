# Task1
number = input("Enter a four-digit number: ")

if len(number) == 4 and number.isdigit():
    first = int(number[0])
    second = int(number[1])
    third = int(number[2])
    forth = int(number[3])
    if (first + forth) == (second - third):
        print("YES")
    else:
        print("NO")
else:
    print("Please enter a four-digit number")

# Task2
age = int(input("Enter your age: "))

if age >= 18:
    print("Access is allowed")
else:
    print("Access denied")

# Task3
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num2 - num1 == num3 - num2:
    print("YES")
else:
    print("NO")

# Task4
x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")

#Task5
x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")

# Task6
a = int(input())
b = int(input())
c = int(input())

num = [a, b, c]
num.sort()
average = num[1]

print(average)

#Task7
month = int(input())

if month == 2:
    days = 28
if month in {4, 6, 9, 11}:
    days = 30
else:
    days = 31

print(days)

# Task8
weight = int(input())

if weight <= 60:
    category = "Lightweight"
if weight <= 64:
    category = "First welterweight"
if weight <= 69:
    category = "Welterweight"
else:
    category = "Unknown"

print(category)

# Task9
pwd = input()
conf = input()

if pwd == conf:
    print("Password accepted")
else:
    print("Password not accepted")

# Task10
a = int(input())
b = int(input())

if a % 2 == 0:
    print("Even")
else:
    print("Odd")
    
# Task11
a = int(input())
b = int(input())

if a < b:
    small = a
else:
    small = b

print(small)

# Task12
age = int(input())

if age <= 13:
    age_group = "childhood"
elif age <= 24:
    age_group = "youth"
elif age <= 59:
    age_group = "maturity"
else:
    age_group = "old age"

print(age_group)

# Task13
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    triangle_type = "Equilateral"
elif a == b or b == c or c == a:
    triangle_type = "Isosceles"
else:
    triangle_type = "Versatile"

print(triangle_type)