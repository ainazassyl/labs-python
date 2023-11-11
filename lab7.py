# Task1
def read_file():
    with open("text1.txt", "r") as file:
        for line in file:
            print(line.strip())

# Task2
import random

def read_random_line():
    with open("file.txt", "r") as file:
        lines = file.readlines()
        return random.choice(lines)
    
# Task3
def count_uppercase():
    with open("file.txt", "r") as file:
        data = file.read()
        count = 0
        for letter in data:
            if letter.isupper():
                count += 1
        return count
    
# Task4
def count_lines():
    with open("file.txt", "r") as file:
        count = 0
        for line in file:
            if not line.startswith("D"):
                count += 1
        return count
    
# Task5
