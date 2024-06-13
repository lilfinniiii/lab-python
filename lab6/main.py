def task1(age):
    try:
        return int(age)
    except ValueError:
        return "Error: Please enter a valid numeric value for age."


def task2(num1, num2):
    try:
        return float(num1) * float(num2)
    except ValueError:
        return "Error: Please enter valid numeric values for numbers."

def task3(s):
    try:
        return len(s)
    except TypeError:
        return "Error: Please enter a string, not a numeric value."


def task4(num_list):
    try:
        return sum(num_list)
    except TypeError:
        return None

def task5(data):
    try:
        result = []
        for name, grades in data:
            avg_grade = sum(grades) / len(grades)
            result.append((avg_grade, name))
        return result
    except Exception as e:
        return "List processing error!"

# Завдання 1
print(task1("25"))  # Очікуваний результат: 25
print(task1("abc"))  # Очікуваний результат: "Error: Please enter a valid numeric value for age."

# Завдання 2
print(task2(5, 3))  # Очікуваний результат: 15.0
print(task2(5, "abc"))  # Очікуваний результат: "Error: Please enter valid numeric values for numbers."

# Завдання 3
print(task3("Hello World!"))  # Очікуваний результат: 12
print(task3(12345))  # Очікуваний результат: "Error: Please enter a string, not a numeric value."

# Завдання 4
print(task4([1, 2, 3, 4, 5]))  # Очікуваний результат: 15
print(task4([1, 2, "three", 4, 5]))  # Очікуваний результат: None

# Завдання 5
data = [('John', (2, 2, 3)), ('Jane', (4, 3, 5)), ('Jack', (5, 4, 4))]
print(task5(data))  # Очікуваний результат: [(2.3333333333333335, 'John'), (4.0, 'Jane'), (4.333333333333333, 'Jack')]
data_with_error = [('John', (2, 2, 3)), ('Jane', 'abc'), ('Jack', (5, 4, 4))]
print(task5(data_with_error))  # Очікуваний результат: "List processing error!"
