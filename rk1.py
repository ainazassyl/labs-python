name = input("Enter your name please: ")
while True:
    salary = input("Enter your desired salary level: ")
    if salary.isdigit():
        salary = int(salary)
        break
    else:
        print(name + ", please enter your desired salary as a digit.")
tax = salary * 0.2
print(name + ", the tax level you will pay with the salary", salary, "is", tax)


#2
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponentiate(x, y):
    return x ** y

print("Please choose the task you want to perform:")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Exponentiation")

choice = input("User Input: ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Please enter the first number:"))
    num2 = float(input("Please enter the second number:"))

    if choice == '1':
        print(add(num1, num2))
    elif choice == '2':
        print(multiply(num1, num2))
    elif choice == '3':
        print(divide(num1, num2))
    elif choice == '4':
        print(exponentiate(num1, num2))
else:
    print("Invalid input")

3
dlina = int(input("Please enter the length of Fibonacci sequence: "))
fibonacci = [1, 1]
for i in range(2, dlina):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print("The Fibonacci sequence for", dlina, "is")
print(*fibonacci, sep=", ")

# 4

unique_items = set()
not_unique = []
print("Please choose the task you want to perform:")
print("1. Enter items")
print("2. Exit")

while True:
    choice = input("User Input: ")

    if choice == '1':
        items = input("Please enter items separated by comma: ")
        items_list = items.split(", ")

        for item in set(items_list):
            if items_list.count(item) > 1:
                not_unique.append((item, items_list.count(item)))
            else:
                unique_items.add(item)

        print("Items are saved")
        print("Unique items:", unique_items)
        print("Not unique items:", tuple(not_unique))
    elif choice == '2':
        break
    else:
        print("Invalid input")


#5
list_of_tasks = []
completed_tasks = []

while True:
    print("Please choose the task you want to perform:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. View All Completed Tasks")
    print("5. Exit")

    choice = input()

    if choice == "1":
        task = input("Enter the task: ")
        list_of_tasks.append(task)
        print(f"The task \"{task}\" was added to the todo list")

    elif choice == "2":
        print("All Tasks:")
        for task in list_of_tasks:
            print(task)

    elif choice == "3":
        task = input("Enter the name of the task: ")
        if task in list_of_tasks:
            list_of_tasks.remove(task)