# Task1.1
inp = input("Enter a string with whitespaces: ")
lower_case = inp.lower()
list = list(lower_case) 
print("Created list is: ")
print(list)

# Task1.2
inp = input("Enter a string with whitespaces: ")
lower_case = inp.lower()
list = list(lower_case)
freq_dict = {}
for symbol in list:
    if symbol in freq_dict:
        freq_dict[symbol] += 1
    else:
        freq_dict[symbol] = 1
freq_list = list(freq_dict.items())
print(freq_list)

# Task1.3
inp = input("Enter a string with whitespaces: ")
lower_case = inp.lower()
list = list(lower_case)
freq_dict = {}

list_vow = []
list_cons = []
list_symb = []
vowels = 'aeiou'

for symbol in freq_dict.keys():
    if symbol in vowels:
        list_vow.append((symbol, freq_dict[symbol]))
    elif symbol.isalpha():
        list_cons.append((symbol, freq_dict[symbol]))
    else:
        list_symb.append((symbol, freq_dict[symbol]))

print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_symb =", list_symb)

# Task1.4
def divide_into_quartiles(list_A):

    list_A.sort()
    length_of_list = len(list_A)
    index_Q2 = int(length_of_list * 0.25)
    index_Q3 = int(length_of_list * 0.5)
    index_Q4 = int(length_of_list * 0.75)
    
    q1 = list_A[:index_Q2] + ([0] if length_of_list % 2 == 1 else [])
    q2 = list_A[index_Q2:index_Q3]
    q3 = list_A[index_Q3:index_Q4]
    q4 = list_A[index_Q4:]
    return q1, q2, q3, q4

# Task2.1
name = 'Adam'
assignment = [82, 56, 44, 30]
lab = [78.20, 77.20]
test = [78, 77]

student = {
    'name': name,
    'assignment': assignment,
    'test': test,
    'lab': lab
}

print("student =", student)

# Task2.2
name = 'Adam'
assignment = [82, 56, 44, 30]
lab = [78.20, 77.20]
test = [78, 77]

student = {
    'name': name,
    'assignment': assignment,
    'test': test,
    'lab': lab
}

sub_assign = len(student.get('assignment', []))
sub_tests = len(student.get('test', []))
sub_labs = len(student.get('lab', []))
total = sub_assign + sub_tests + sub_labs

submission_check = {student['name']: total}
print(submission_check)

# Task2.3
def calc_final(student):
    if len(student['assignment']) < 4 or len(student['lab']) < 2 or len(student['test']) < 2:
        student['final_grade'] = 0
    else:
        avg_assign = sum(student['assignment']) / len(student['assignment'])
        avg_lab = sum(student['lab']) / len(student['lab'])
        avg_test = sum(student['test']) / len(student['test'])
        final = 0.3 * avg_assign + 0.5 * avg_lab + 0.2 * avg_test
        student['final_grade'] = round(final, 2)

student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
sub_rate = {'Adam': 6}
calc_final(student)
print(student)

student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2]}
sub_rate = {'Adam': 6, 'Kevin': 3}
calc_final(student2)
print(student2)

# Task2.4
name = 'Adam'
assignment = [82, 56, 44, 30]
lab = [78.20, 77.20]
test = [78, 77]
final = [70.25]

student1 = {
    'name': name,
    'assignment': assignment,
    'test': test,
    'lab': lab,
    'final_grade': final
}

name2 = 'Kevin'
assignment2 = [82, 30]
lab2 = [78.2]
test2 = []
final2 = [0]

student2 = {
    'name': name2,
    'assignment': assignment2,
    'test': test2,
    'lab': lab2,
    'final_grade': final2
}

students = {}

for stu_dict in [student1, student2]:
    stu_name = stu_dict['name']
    stu_info = {key: value for key, value in stu_dict.items() if key != 'name'}
    students[stu_name] = stu_info

print("students = ", students)

# Task3.1
from collections import defaultdict
transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]

stats = defaultdict(lambda: {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None})

for user_id, transaction_type in transactions:
    stats[user_id][transaction_type] += 1

for user, transactions_info in stats.items():
    max_trans = max(transactions_info, key=lambda k: transactions_info[k] if k in (1, 2, 3) else -1)
    min_trans = min(transactions_info, key=lambda k: transactions_info[k] if k in (1, 2, 3) else float('inf'))
    transactions_info['mft'] = max_trans
    transactions_info['lft'] = min_trans

stats = dict(stats)
print("stats = ", stats)



