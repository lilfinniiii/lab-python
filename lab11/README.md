# Лабораторна робота №11: Масиви в Python

## 2.2 Мета роботи
Метою лабораторної роботи є виконання завдань з використанням масивів у мові програмування Python.

## 2.3 Опис завдання

### Завдання 1: Sum of Squares
Create a function `task1` that accepts an array of numbers and returns the sum of the squares of each number.

### Завдання 2: Filter and Sum
Create a function `task2` that accepts an array of numbers and returns the sum of all the elements that are greater or equal than the average of the array.

### Завдання 3: Sort by Frequency
Create a function `task3` that sorts an array of numbers based on the frequency of each element from highest to lowest. If two numbers have the same frequency, the smaller number should come first.

### Завдання 4: Find Missing Number
Create a function `task4` that finds the missing number in an array containing all integers from 1 to n except one. Assume the array has no duplicates.

### Завдання 5: Longest Consecutive Sequence
Create a function `task5` that finds the length of the longest consecutive elements sequence in an unsorted array.

### Завдання 6: Rotate Array
Create a function `task6` that rotates the array to the right by k steps, where k is non-negative.

### Завдання 7: Array of Products
Create a function `task7` that calculates an array of products of all numbers except the one at the current index without using division.

### Завдання 8: Maximum Subarray Sum
Create a function `task8` that finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers.

### Завдання 9: Spiral Order Matrix
Create a function `task9` that returns all elements of a 2D matrix in spiral order.

### Завдання 10: K Closest Points to Origin
Create a function `task10` that finds the k closest points to the origin (0, 0) in a 2D plane, given an array of coordinate points.

## 2.4 Виконання роботи

### Завдання 1: Sum of Squares
Код функції `task1`:
```python
def task1(arr):
    return sum(number**2 for number in arr)
```
### Завдання 2: Filter and Sum
Код функції `task2`:
```python
def task2(arr):
    avg = sum(arr)/len(arr)
    return sum(number for number in arr if number >= avg)
```
### Завдання 3: Sort by Frequency
Код функції `task3`:
```python
from collections import Counter

def task3(arr):
    count = Counter(arr)
    
    sorted_arr = sorted(arr, key=lambda x: (-count[x], x))
    
    return sorted_arr
```
### Завдання 4: Find Missing Number
Код функції `task4`:
```python
def task4(arr):
    for i in range(1, arr[-1]):
        if not i in arr:
            return i
```
### Завдання 5: Longest Consecutive Sequence
Код функції `task5`:
```python
def task5(arr):
    arr.sort()
    
    longest_streak = 1
    current_streak = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_streak += 1
        elif arr[i] != arr[i - 1]:
            current_streak = 1
        
        longest_streak = max(longest_streak, current_streak)
    
    return longest_streak
```
### Завдання 6: Rotate Array
Код функції `task6`:
```python
def task6(arr, k):
    if not arr:
        return arr
    k %= len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    return arr
```
### Завдання 7: Array of Products
Код функції `task7`:
```python
def task7(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    
    products = [left_products[i] * right_products[i] for i in range(n)]
    
    return products
```
### Завдання 8: Maximum Subarray Sum
Код функції `task8`:
```python
def task8(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```
### Завдання 9: Spiral Order Matrix
Код функції `task9`:
```python
def task9(matrix):
    if not matrix:
        return []
    result = []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

```
### Завдання 10: K Closest Points to Origin
Код функції `task10`:
```python
import heapq
def task10(points, k):
    if not points or k <= 0:
        return []
    heap = []
    for point in points:
        distance = point[0] ** 2 + point[1] ** 2
        heapq.heappush(heap, (distance, point))
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    return result
points = [(1, 3), (-2, 2), (5, 8), (-1, 0), (0, 0), (3, 4)]
k = 3
```
## 2.5 Результати
```python
print(task1([1, 2, 3]))   # Output: 14
print(task2([1, 2, 3, 4, 10])) # Output: 14 
print(task3([4, 6, 2, 6, 4, 4, 6])) # Output: [4, 4, 4, 6, 6, 6, 2] 
print(task4([1, 2, 4, 5])) # Output: 3 
print(task5([100, 4, 200, 1, 3, 2])) # Output: 4 
print(task6([1, 2, 3, 4, 5], 2)) # Output: [4, 5, 1, 2, 3] 
print(task7([1, 2, 3, 4])) # Output: [24, 12, 8, 6]
print(task8([-2,1,-3,4,-1,2,1,-5,4])) # Output: 6 
print(task9([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5] 
print(task10([(1, 2), (1, 1), (3, 4)], 2)) # Output: [(1, 1), (1, 2)] 
```

## 2.6 Висновки
У цій лабораторній роботі було виконано завдання з використанням масивів у мові програмування Python

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

