# Task 1.1
sequence = [4, 8, 15, 16, 23, 42]
for number in sequence:
    print(number, end=' ') 

# Task 1.2
sequence = [4, 8, 15, 16, 23, 42]
for number in sequence:
    print(number)

# Task 1.3
try:
    first_number = int(input("Enter the first number: "))
    for i in range(3):
        print(first_number + i)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# Task 1.4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
total_sum = num1 + num2 + num3
print(total_sum)

# Task 1.5
edge_length = float(input("Enter the edge length of the cube: "))
volume = edge_length ** 3
surface_area = 6 * (edge_length ** 2)
print(f"Volume = {int(volume)}")
print(f"Total surface area = {int(surface_area)}")

# Task 2.1
n = int(input("Enter the number of schoolchildren: "))
k = int(input("Enter the total number of tangerines: "))
whole_tangerines_per_student = k // n
remaining_tangerines = k % n
print(whole_tangerines_per_student)
print(remaining_tangerines)

# Task 2.2
number = input("Enter a four-digit number: ")
number = int(number)
thousands_digit = number // 1000
hundreds_digit = (number % 1000) // 100
tens_digit = (number % 100) // 10
units_digit = number % 10
print(f"The digit in the thousands position is {thousands_digit}")
print(f"The digit in the hundreds position is {hundreds_digit}")
print(f"The digit in the tens position is {tens_digit}")
print(f"The digit in the units position is {units_digit}")

# Task 2.3
population = int(input("Enter the population of the universe: "))
if population % 2 == 0:
        survivors = population // 2
else:
        survivors = (population // 2) + 1
print(survivors)

# Task 2.4
num = int(input("Enter a number: "))
result = num << 1
if result == 0:
      print("Warning: The result of << is zero")
else:
     print(f"The result of << is {result}")

# Task 2.5
try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    operation = input("Please choose the operation (+, -, *, /): ")
    if operation == "+":
        result = num1 + num2
    if operation == "-":
        result = num1 - num2
    if operation == "*":
        result = num1 * num2
    if operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
    if 'result' in locals():
        print(f"{num1} {operation} {num2} = {result:.3f}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
    