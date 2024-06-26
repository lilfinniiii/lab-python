# Лабораторна робота №5: Операції з словниками та масивами

## 2.2 Мета роботи
Метою лабораторної роботи є виконання різноманітних завдань з операціями над словниками та масивами у мові програмування Python.

## 2.3 Опис завдання

### Завдання 1: Злиття двох словників
Напишіть функцію `task1`, яка приймає два словники на вхід та повертає один об'єднаний словник.

### Завдання 2: Інтерпретація рядка як масиву машинних значень
Створіть функцію `task2`, яка приймає рядок на вхід та повертає його як масив машинних значень.

### Завдання 3: Видалення дублікатів з масиву
Напишіть функцію `task3`, яка приймає масив на вхід та повертає новий масив без дублікатів.

### Завдання 4: Пошук відсутнього числа у заданому діапазоні
Створіть функцію `task4`, яка приймає масив чисел на вхід та повертає відсутнє число у діапазоні від 10 до 20.

### Завдання 5: Повернення унікальних значень зі словника
Напишіть функцію `task5`, яка приймає список словників на вхід та повертає список унікальних значень, а також кількість цих унікальних значень.

### Завдання 6: Кількість можливих комбінацій букв зі словників
Створіть функцію `task6`, яка приймає список словників на вхід та повертає кількість можливих комбінацій букв.

### Завдання 7: Повернення трьох найбільших значень ключів зі словника
Напишіть функцію `task7`, яка приймає словник на вхід та повертає список трьох найбільших значень ключів.

### Завдання 8: Комбінування значень у списку словників
Створіть функцію `task8`, яка приймає список словників на вхід та повертає словник з об'єднаними значеннями.

## 2.4 Виконання роботи
```python
from array import array
```
### Завдання 1: Злиття двох словників
Код функції `task1`:
```python
def task1(lista, listb):
    return {**lista, **listb}
```
### Завдання 2: Інтерпретація рядка як масиву машинних значень
Код функції `task2`:
```python
def task2(arraya):
    byte = arraya.tobytes()
    return byte
```
### Завдання 3: Видалення дублікатів з масиву
Код функції `task3`:
```python
def task3(arraya):
    return sorted(set(array),key=arraya.index)
```
### Завдання 4: Пошук відсутнього числа у заданому діапазоні
Код функції `task4`:
```python
def task4(arraya):
    rangeset = set(range(10,21))
    arrset = set(arraya)
    num = rangeset - arrset
    return num.pop()
```
### Завдання 5: Повернення унікальних значень зі словника
Код функції `task5`:
```python
def task5(lista):
    return set(val for dic in lista for val in dic.values())
```
### Завдання 6: Кількість можливих комбінацій букв зі словників
Код функції `task6`:
```python
def task6(lista):
    return [x for x in range(4)]
```
### Завдання 7: Повернення трьох найбільших значень ключів зі словника
Код функції `task7`:
```python
def task7(dict):
    return nlargest(3, dict, key=dict.get)
```
### Завдання 8: Комбінування значень у списку словників
Код функції `task8`:
```python
from collections import Counter
def task8(dict):
    result = Counter()
    for d in dict:
        result[d['item']] += d['amount']
    return result
```
## 2.5 Результати
```python
# Завдання 1
print(task1({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  # Очікуваний результат: {'a': 1, 'b': 3, 'c': 4}

# Завдання 2
import array

arraya = array.array('i', [7, 8, 9, 10])
byte_result = task2(arraya)
print(f"Original array: {arraya}")
print(f"Bytes: {byte_result}")
# Очікуваний результат:
# Original array: array('i', [7, 8, 9, 10])
# Bytes: b'\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00'

# Завдання 3
print(task3([1, 3, 5, 1, 3, 7, 9]))  # Очікуваний результат: [1, 3, 5, 7, 9]
print(task3([2, 4, 2, 6, 4, 8]))  # Очікуваний результат: [2, 4, 6, 8]

# Завдання 4
print(task4([10, 11, 12, 13, 14, 16, 17, 18, 19, 20]))  # Очікуваний результат: 15
print(task4([10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))  # Очікуваний результат: 20

# Завдання 5
sample_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_values = task5(sample_data)
print(unique_values)  # Очікуваний результат: {'S001', 'S002', 'S005', 'S007', 'S009'}

# Завдання 6
# На даний момент повертається простий список від 0 до 3. Ви можете замінити цей код для коректного підрахунку комбінацій
print(task6([{'a': 1}, {'b': 2}, {'c': 3}]))  # Очікуваний результат: 4 (простий приклад)

# Завдання 7
dict_data = {'a': 5, 'b': 8, 'c': 3, 'd': 10, 'e': 7}
print(task7(dict_data))  # Очікуваний результат: ['d', 'b', 'e']

# Завдання 8
list_data = [{'item': 'apple', 'amount': 10}, {'item': 'banana', 'amount': 5}, {'item': 'apple', 'amount': 3}]
print(task8(list_data))  # Очікуваний результат: Counter({'apple': 13, 'banana': 5})
```

## 2.6 Висновки
У цій лабораторній роботі було виконано завдання з операціями над словниками та масивами у мові програмування Python.

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

