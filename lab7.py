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
        random_line = random.choice(lines)
        print(random_line.strip())
    
# Task3
def count_uppercase():
    with open("file.txt", "r") as file:
        content = file.read()
        uppercase_count = sum(1 for char in content if char.isupper())
        print("Uppercase character count:", uppercase_count)
    
# Task4
def count_lines():
    with open("file.txt", "r") as file:
        count = sum(1 for line in file if not line.lstrip().startswith('D'))
        print(count)
    
# Task5
def count_words_ending_with_F(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        count = sum(1 for word in words if word.endswith(('F', 'f')))
        print(count)

# Task6
def count_all_and_none_words(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        all_count = content.split().count("all")
        none_count = content.split().count("none")
        print(f'"all" count: {all_count}, "none" count: {none_count}')

# Task7
def count_word_frequency(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        word_frequency = {}
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
        print(word_frequency)

# Task8
def find_longest_word(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        print(longest_word)

# Task9
def correct_characters(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        corrected_content = content.replace('B', 'J')
        print(corrected_content)

# Task10
def count_A_and_B_occurrences(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        count_A = content.lower().count('a')
        count_B = content.lower().count('b')
        print(f'a={count_A}, b={count_B}')
