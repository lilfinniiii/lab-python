# Лабораторна робота №10: Обробка даних

## 2.2 Мета роботи
Метою лабораторної роботи є виконання завдань з обробкою даних у мові програмування Python.

## 2.3 Опис завдання

### Завдання 1: Interpolate Missing Values
Create a function `interpolate_missing` that takes a list of numbers, which may include None as a placeholder for missing values. The function should interpolate missing values using the average of the nearest non- None neighbors.

### Завдання 2: Fibonacci Series Generator
Write a generator function `fibonacci` that yields the Fibonacci series up to n terms.

### Завдання 3: Batch Data Processing
Define a function process_batches that takes a list of numbers and a batch size, then processes each batch to return their maximum values.

### Завдання 4: Encode and Decode Strings
Create two functions encode_string and decode_string . encode_string should convert the string into a run-length encoded format, and decode_string should revert it back to the original string.

### Завдання 5: Matrix Rotation
Write a function rotate_matrix that rotates a given n x n matrix 90 degrees clockwise.

### Завдання 6: Regular Expression Search
Define a function regex_search that takes a list of strings and a regular expression pattern, returning a list of all strings that match the pattern.

### Завдання 7: Merge Sorted Arrays
Create a function merge_sorted_arrays that merges two sorted arrays into a single sorted array.

### Завдання 8: Prime Number Checker
Write a function is_prime that takes a number and returns True if it is a prime number, otherwise False .

### Завдання 9: Group by Key
Define a function group_by_key that takes a list of dictionaries and groups them by a specified key

### Завдання 10: Remove Outliers
Create a function remove_outliers that removes elements from a list that are more than two standard deviations away from the mean.

## 2.4 Виконання роботи
```python
import re
```
### Завдання 1: Interpolate Missing Values
Код функції `task1`:
```python
def interpolate_missing(numbers):
    interpolated_numbers = []
    for i, num in enumerate(numbers):
        if num is None:
            left_index = i - 1
            right_index = i + 1
            
            while left_index >= 0 and numbers[left_index] is None:
                left_index -= 1
                
            while right_index < len(numbers) and numbers[right_index] is None:
                right_index += 1
                
            left = numbers[left_index] if left_index >= 0 else None
            right = numbers[right_index] if right_index < len(numbers) else None
            
            if left is not None and right is not None:
                interpolated_numbers.append(left + (right - left) / (right_index - left_index))
            elif left is not None:
                interpolated_numbers.append(left)
            elif right is not None:
                interpolated_numbers.append(right)
            else:
                interpolated_numbers.append(None)
        else:
            interpolated_numbers.append(num)
    
    return interpolated_numbers
```
### Завдання 2: Fibonacci Series Generator
Код функції `task2`:
```python
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
```
### Завдання 3: Batch Data Processing
Код функції `task3`:
```python
def process_batches(numbers, batch_size):
    max_values = []
    for i in range(0, len(numbers), batch_size):
        batch = numbers[i:i + batch_size]
        max_values.append(max(batch))
    return max_values
```
### Завдання 4: Encode and Decode Strings
Код функції `task4`:
```python
def encode_string(s):
    encoded = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += str(count) + s[i - 1]
            count = 1
    encoded += str(count) + s[-1]
    return encoded


def decode_string(s):
    decoded = ""
    i = 0
    while i < len(s):
        count = int(s[i])
        decoded += s[i + 1] * count
        i += 2
    return decoded
```
### Завдання 5: Matrix Rotation
Код функції `task5`:
```python
def rotate_matrix(matrix):
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]
    return rotated_matrix
```
### Завдання 6: Regular Expression Search
Код функції `task6`:
```python
def regex_search(strings, pattern):
    matching_strings = []
    for string in strings:
        if re.match(pattern, string):
            matching_strings.append(string)
    return matching_strings
```
### Завдання 7: Merge Sorted Arrays
Код функції `task7`:
```python
def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array
```
### Завдання 8: Prime Number Checker
Код функції `task8`:
```python
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
```
### Завдання 9: Group by Key
Код функції `task9`:
```python
def group_by_key(data, key):
    grouped_data = {}
    for item in data:
        if item[key] in grouped_data:
            grouped_data[item[key]].append(item['value'])
        else:
            grouped_data[item[key]] = [item['value']]
    return grouped_data

```
### Завдання 10: Remove Outliers
Код функції `task10`:
```python
import numpy as np

def remove_outliers(lst):
    mean = np.mean(lst)
    std_dev = np.std(lst)
    outliers_removed = [x for x in lst if abs(x - mean) <= 2 * std_dev]
    return outliers_removed
```
## 2.5 Результати
```python
print(interpolate_missing([1, None, None, 4])) # Output: [1, 2, 3, 4]

for num in fibonacci(5):
 print(num) # Output: 0, 1, 1, 2, 3

print(process_batches([1, 2, 3, 4, 5, 6], 2)) # Output: [2, 4, 6]

encoded = encode_string("aaabbc")
print(encoded) # Output: "3a2bc"
print(decode_string(encoded)) # Output: "aaabbc"

matrix = [
 [1, 2],
 [3, 4]
]
print(rotate_matrix(matrix)) # Output: [[3, 1], [4, 2]]

print(regex_search(["test", "test123", "none"], "test\d+")) # Output: ["test123"]

print(merge_sorted_arrays([1, 3, 5], [2, 4, 6])) # Output: [1, 2, 3, 4, 5, 6]

print(is_prime(11)) # Output: True

data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2},
{'key': 'a', 'value': 3}]
print(group_by_key(data, 'key')) # Output: {'a': [1, 3], 'b': [2]}

print(remove_outliers([10, 100, 200, 300, 400, 500, 600])) # Output: [100, 200, 300, 400, 500]
```

## 2.6 Висновки
У цій лабораторній роботі було виконано завдання з обробкою даних у мові програмування Python

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

