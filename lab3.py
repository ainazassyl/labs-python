# Task1
N = int(input("Enter a number: "))
even_number = 2
while even_number <= N:
    print(even_number)
    even_number += 2

# Task2
N = int(input("Enter a number: "))
fac = 1
current = 1
while current <= N:
    fac *= current
    current += 1
print(f"The factorial of {N} is {factorial}")

# Task3
while True:
    number = int(input("Enter a number: "))
    if number == 42:
        print("You entered 42. Terminating the program.")
        break

# Task4
input_string = input("Enter a string: ")
count_a = input_string.count('a')
print(f"The number of 'a's in the string is: {count_a}")

# Task5
num_str = input("Enter a number: ")
digit_sum = 0
for char in num_str:
    if char.isdigit():
        digit_sum += int(char)

print(f"The sum of digits in the number is: {digit_sum}")

# Task6
N = int(input("Enter a positive integer (N): "))
fibonacci_a, fibonacci_b = 0, 1
count = 0
while count < N:
    print(fibonacci_a, end=" ")
    fibonacci_a, fibonacci_b = fibonacci_b, fibonacci_a + fibonacci_b
    count += 1

# Task7
input_string = input("Enter a string: ")
reversed_string = input_string[::-1]
print("Reversed string:", reversed_string)

# Task8
odd_sum = 0
while True:
    number = int(input("Enter a number (0 to stop):"))
    
    if number == 0:
        break

    if number % 2 == 0:
        continue

    odd_sum += number

print(f"The sum of odd numbers is: {odd_sum}")

# Task9
import random
target_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (between 1 and 100): "))

    if guess < target_number:
        print("Too small.")
    elif guess > target_number:
        print("Too large.")
    else:
        print("Congratulations! You guessed the number.")
        break

# Task10
input_string = input("Enter a string: ")
cleaned_string = input_string.replace(" ", "").lower()
if cleaned_string == cleaned_string[::-1]:
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")

# Task11
X = float(input("Enter the base (X): "))
Y = int(input("Enter the exponent (Y): "))
result = 1
while Y > 0:
    result *= X
    Y -= 1

print(f"{X} to the power of {Y} is {result}")

# Task12
N = int(input("Enter a positive integer (N): "))
num = 2

print("Prime numbers in the range from 1 to", N, "are:")
while num <= N:
    is_prime = True
    divisor = 2

    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break 
        divisor += 1

    if is_prime:
        print(num, end=" ")

    num += 1

# Task13
num_str = input("Enter a number: ")
reversed_num_str = num_str[::-1]
print("Reversed number:", reversed_num_str)

# Task14
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

while True:
    if is_prime(num):
        print(f"{num} is a prime number.")
        break
    else:
        print(f"{num} is not a prime number.")
        num += 1

# Task15
input_string = input("Enter a string: ")
shift = int(input("Enter the shift value (N): "))

encrypted_string = ""

for char in input_string:
    if char.isalpha():
        shift_amount = shift % 26  # Ensure the shift wraps around the alphabet cyclically
        if char.islower():
            new_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
        elif char.isupper():
            new_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
    else:
        new_char = char

    encrypted_string += new_char

print("Encrypted string:", encrypted_string)