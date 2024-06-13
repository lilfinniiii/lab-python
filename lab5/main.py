from array import array

def task1(lista, listb):
    return {**lista, **listb}
def task2(arraya):
    byte = arraya.tobytes()
    return byte
def task3(arraya):
    return sorted(set(array),key=arraya.index)
def task4(arraya):
    rangeset = set(range(10,21))
    arrset = set(arraya)
    num = rangeset - arrset
    return num.pop()
def task5(lista):
    return set(val for dic in lista for val in dic.values())
def task6(lista):
    return [x for x in range(4)]
from heapq import nlargest
def task7(dict):
    return nlargest(3, dict, key=dict.get)
from collections import Counter
def task8(dict):
    result = Counter()
    for d in dict:
        result[d['item']] += d['amount']
    return result

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



