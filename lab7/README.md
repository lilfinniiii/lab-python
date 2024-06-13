# Лабораторна робота №7: Обробка даних та обробка помилок у Python

## 2.2 Мета роботи
Метою лабораторної роботи є виконання різноманітних завдань з обробкою даних та обробкою помилок у мові програмування Python.

## 2.3 Опис завдання

### Завдання 1: Повернення цілого числа
Напишіть функцію `task1`, яка приймає ціле число та повертає його. Якщо користувач вводить нечислове значення, програма повинна повернути повідомлення про помилку: “Error: Please enter a valid numeric value for age.”

### Завдання 2: Множення двох чисел
Створіть функцію `task2`, яка приймає два числа та повертає їхній добуток. Якщо користувач вводить нечислове значення, програма повинна повернути повідомлення про помилку: "Error: Please enter valid numeric values for numbers."

### Завдання 3: Довжина рядка
Напишіть функцію `task3`, яка приймає рядок та повертає його довжину. Якщо користувач не вводить рядок, програма повинна повернути повідомлення про помилку: "Error: Please enter a string, not a numeric value."

### Завдання 4: Сума списку цілих чисел
Створіть функцію `task4`, яка приймає список цілих чисел та повертає їхню суму. Якщо список містить значення, яке не є цілим числом, програма повинна повернути None.

### Завдання 5: Середній бал студентів
Напишіть функцію `task5`, яка приймає список кортежів, де кожен кортеж містить ім'я студента та його оцінки, і повертає список кортежів, де перший елемент - середній бал студента, а другий елемент - ім'я студента. Якщо при обробці списку виникає помилка, функція повинна повернути рядок "List processing error!".

## 2.4 Виконання роботи

### Завдання 1: Злиття двох словників
Код функції `task1`:
```python
def task1(age):
    try:
        return int(age)
    except ValueError:
        return "Error: Please enter a valid numeric value for age."
```
### Завдання 2: Інтерпретація рядка як масиву машинних значень
Код функції `task2`:
```python
def task2(num1, num2):
    try:
        return float(num1) * float(num2)
    except ValueError:
        return "Error: Please enter valid numeric values for numbers."
```
### Завдання 3: Видалення дублікатів з масиву
Код функції `task3`:
```python
def task3(s):
    try:
        return len(s)
    except TypeError:
        return "Error: Please enter a string, not a numeric value."
```
### Завдання 4: Пошук відсутнього числа у заданому діапазоні
Код функції `task4`:
```python
def task4(num_list):
    try:
        return sum(num_list)
    except TypeError:
        return None
```
### Завдання 5: Повернення унікальних значень зі словника
Код функції `task5`:
```python
def task5(data):
    try:
        result = []
        for name, grades in data:
            avg_grade = sum(grades) / len(grades)
            result.append((avg_grade, name))
        return result
    except Exception as e:
        return "List processing error!"
```

## 2.5 Результати
```python
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

```

## 2.6 Висновки
У цій лабораторній роботі було виконано завдання з обробкою даних та обробкою помилок у мові програмування Python.

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

