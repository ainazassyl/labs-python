# Task1.1
def get_keys_with_value_true(dict):
    true_keys = []
    for key, value in dict.items():
        if value == True:
            true_keys.append(key)
    return true_keys

my_dict = {'a': True, 'b': False, 'c': True}
result = get_keys_with_value_true(my_dict)
print(result)

# Task1.2
def get_unique_elements(list):
    unique_list = []
    for num in list:
        if list.count(num) == 1:
            unique_list.append(num)
    return unique_list

input_list = [1, 2, 3, 1, 2, 4]
output = get_unique_elements(input_list)
print(output)

# Task1.3
def get_date_in_format(date):
    date_parts = date.split('.')
    day = date_parts[2]
    month = date_parts[1]
    year = date_parts[0]
    return f"{day}.{month}.{year}"

input = "2023.10.23"
formatted = get_date_in_format(input)
print(formatted)

# Task1.4
def get_elements_with_no_more_than_two_occurrences(list):
    unique_lst = []
    for num in list:
        if list.count(num) <= 2:
            unique_lst.append(num)
    return unique_lst

input_list = [1, 2, 3, 1, 2, 4]
result = get_elements_with_no_more_than_two_occurrences(input_list)
print(result)

# Task1.5
def get_words_from_string(string):
    words = string.split()
    return words

input_string = "This a string with a several words."
result = get_words_from_string(input_string)
print(result)

# Task2.6
def get_unique_elements_with_count(list):
    unique_dict = {}
    for num in list:
        if num in unique_dict:
            unique_dict[num] += 1
        else:
            unique_dict[num] = 1
    return unique_dict

input_list = [1, 2, 3, 1, 2, 4, 1, 2]
result = get_unique_elements_with_count(input_list)
print(result)

# Task2.7
def get_prime_numbers(n):
    primes = []
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

n = 100
result = get_prime_numbers(n)
print(result)

# Task2.8
def get_prime_numbers_in_list(list):
    primes = []
    for num in list:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 
99]
result = get_prime_numbers_in_list(input_list)
print(result)

# Task2.9
from datetime import datetime

def get_difference_between_dates(date1, date2):
    date_format = "%Y.%m.%d"
    date1_obj = datetime.strptime(date1, date_format)
    date2_obj = datetime.strptime(date2, date_format)
    delta = date2_obj - date1_obj
    return delta.days

start_date = "2023.10.23"
end_date = "2023.10.24"
difference = get_difference_between_dates(start_date, end_date)
print(f"The difference between {start_date} and {end_date} is {difference} days.")

# Task3.10
def get_decimal_number_from_binary_string(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number

binary_string = "10110011"
result = get_decimal_number_from_binary_string(binary_string)
print(result)

# Task3.11
def is_perfect_square(num):
    return int(num**0.5)**2 == num

def get_perfect_squares(lst):
    return all(is_perfect_square(num) for num in lst)

input_list = [4, 25, 81]
result = get_perfect_squares(input_list)
print(result)

# Task3.12
def sort_by_price(shopping_list):
    sorted_list = sorted(shopping_list, key=lambda x: x['price'])
    return sorted_list

shopping_list = [
    {"name": "Apple", "price": 100},
    {"name": "Banana", "price": 50},
    {"name": "Orange", "price": 20}
]

sorted_shopping_list = sort_by_price(shopping_list)
print(sorted_shopping_list)

# Task3.13
def get_words_starting_with_vowel(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_words = [word for word in words if word[0].lower() in vowels]
    return vowel_words

input_words = ["apple", "banana", "orange", "bear", "cat"]
result = get_words_starting_with_vowel(input_words)
print(result)
