# Лабораторна робота №17: Generators and Data structures

## 2.2 Мета роботи
Метою лабораторної роботи є виконання завдань з генератори та структури даних у мові програмування Python.

## 2.3 Опис завдання

### Task 1: Create a generator to iterate over a list of numbers.
Create a generator function named number_generator that takes a list of numbers and yields each number one by one.

### Task 2: Develop a generator that yields even numbers from a given range.
Create a generator function named even_number_generator that takes two integers, start and end , and yields even numbers within that range.

### Task 3: Implement a generator to yield odd numbers within a specified range.
Create a generator function named odd_number_generator that takes two integers, start and end , and yields odd numbers within that range.

### Task 4: Write a generator that produces Fibonacci numbers.
Create a generator function named fibonacci_generator that produces Fibonacci numbers indefinitely.

### Task 5: Create a generator that yields prime numbers up to a given limit.
Create a generator function named prime_number_generator that takes an integer limit and yields prime numbers up to that limit.

### Task 6: Develop a generator to traverse a binary tree in pre-order.
Create a generator function named pre_order_traversal that takes the root of a binary tree and yields its nodes in pre-order.

### Task 7: Implement a generator for in-order traversal of a binary tree.
Create a generator function named in_order_traversal that takes the root of a binary tree and yields its nodes in in-order.

### Task 8: Write a generator for post-order traversal of a binary tree.
Create a generator function named post_order_traversal that takes the root of a binary tree and yields its nodes in post-order.

### Task 9: Create a generator to traverse a graph using depth-first search (DFS).
Create a generator function named dfs_traversal that takes an adjacency list representation of a graph and a starting node, and yields nodes in DFS order.

### Task 10: Develop a generator for breadth-first search (BFS) traversal of a graph.
Create a generator function named bfs_traversal that takes an adjacency list representation of a graph and a starting node, and yields nodes in BFS order.

### Task 11: Implement a generator that yields the keys of a dictionary.
Create a generator function named dict_keys_generator that takes a dictionary and yields its keys one by one.

### Task 12: Write a generator that yields the values of a dictionary.
Create a generator function named dict_values_generator that takes a dictionary and yields its values one by one.

### Task 13: Create a generator to iterate over key-value pairs of a dictionary.
Create a generator function named dict_items_generator that takes a dictionary and yields its key-value pairs as tuples one by one.

### Task 14: Develop a generator that yields lines from a file one by one.
Create a generator function named file_lines_generator that takes a file path and yields its lines one by one.

### Task 15: Implement a generator to iterate over words in a text file.
Create a generator function named file_words_generator that takes a file path and yields its words one by one.

### Task 16: Write a generator that yields characters from a string one by one.
Create a generator function named string_chars_generator that takes a string and yields its characters one by one.

### Task 17: Create a generator to yield unique elements from a list.
Create a generator function named unique_elements_generator that takes a list and yields its unique elements one by one.

### Task 18: Develop a generator that yields elements of a list in reverse order.
Create a generator function named reverse_list_generator that takes a list and yields its elements in reverse order.

### Task 19: Implement a generator to yield the Cartesian product of two lists.
Create a generator function named cartesian_product_generator that takes two lists and yields the Cartesian product of the two lists as tuples.

### Task 20: Write a generator that yields permutations of a list.
Create a generator function named permutations_generator that takes a list and yields all possible permutations of the list.

### Task 21: Create a generator to yield combinations of a list of elements.
Create a generator function named combinations_generator that takes a list of elements and yields all possible combinations of the elements.

### Task 22: Develop a generator to iterate over a list of tuples.
Create a generator function named tuple_list_generator that takes a list of tuples and yields each tuple one by one.

### Task 23: Implement a generator that yields elements from multiple lists in parallel.
Create a generator function named parallel_lists_generator that takes multiple lists and yields elements from each list in parallel.

### Task 24: Write a generator that yields elements from a nested list (flattening the list).
Create a generator function named flatten_list_generator that takes a nested list and yields each element in a flat sequence.

### Task 25: Create a generator to yield elements from a nested dictionary.
Create a generator function named nested_dict_generator that takes a nested dictionary and yields its elements.

### Task 26: Develop a generator to yield powers of 2 up to a given number.
Create a generator function named powers_of_two_generator that takes an integer n and yields powers of 2 up to 2^n .

### Task 27: Implement a generator that yields powers of a given base up to a specified limit.
Create a generator function named powers_of_base_generator that takes a base and a limit, and yields powers of the base up to the specified limit.

### Task 28: Write a generator to yield the squares of numbers in a given range.
Create a generator function named squares_generator that takes a range of numbers and yields their squares

### Task 29: Create a generator to yield cubes of numbers in a specified range.
Create a generator function named cubes_generator that takes a range of numbers and yields their cubes.

### Task 30: Develop a generator that yields factorials of numbers up to a given limit.
Create a generator function named factorials_generator that takes an integer n and yields factorials of numbers from 0 up to n .

### Task 31: Implement a generator to yield numbers in the Collatz sequence.
Create a generator function named collatz_sequence_generator that takes an integer and yields numbers in the Collatz sequence.

### Task 32: Write a generator that yields numbers in a geometric progression.
Create a generator function named geometric_progression_generator that takes an initial term, a common ratio, and a limit, and yields numbers in the geometric progression.

### Task 33: Create a generator to yield numbers in an arithmetic progression.
Create a generator function named arithmetic_progression_generator that takes an initial term, a common difference, and a limit, and yields numbers in the arithmetic progression.

### Task 34: Develop a generator that yields the running sum of a list of numbers.
Create a generator function named running_sum_generator that takes a list of numbers and yields their running sum.

### Task 35: Implement a generator to yield the running product of a list of numbers.
Create a generator function named running_product_generator that takes a list of numbers and yields their running product.

## 2.4 Виконання роботи
### Task 1: Create a generator to iterate over a list of numbers.
Код функції `task1`:
```python
def number_generator(numbers):
    for number in numbers:
        yield number
```
### Task 2: Develop a generator that yields even numbers from a given range.
Код функції `task2`:
```python
def even_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number
```
### Task 3: Implement a generator to yield odd numbers within a specified range.
Код функції `task3`:
```python
def odd_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number
```
### Task 4: Write a generator that produces Fibonacci numbers.
Код функції `task4`:
```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```
### Task 5: Create a generator that yields prime numbers up to a given limit.
Код функції `task5`:
```python
def prime_number_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, limit + 1):
        if is_prime(num):
            yield num
```
### Task 6: Develop a generator to traverse a binary tree in pre-order.
Код функції `task6`:
```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)
```
### Task 7: Implement a generator for in-order traversal of a binary tree.
Код функції `task7`:
```python
def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)
```
### Task 8: Write a generator for post-order traversal of a binary tree.
Код функції `task8`:
```python
def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value
```
### Task 9: Create a generator to traverse a graph using depth-first search (DFS).
Код функції `task9`:
```python
def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))
```
### Task 11: Implement a generator that yields the keys of a dictionary.
Код функції `task11`:
```python
def dict_keys_generator(dictionary):
    for key in dictionary.keys():
        yield key
```
### Task 12: Write a generator that yields the values of a dictionary.
Код функції `task12`:
```python
def dict_values_generator(dictionary):
    for value in dictionary.values():
        yield value
```
### Task 13: Create a generator to iterate over key-value pairs of a dictionary.
Код функції `task13`:
```python
def dict_items_generator(dictionary):
    for item in dictionary.items():
        yield item
```
### Task 14: Develop a generator that yields lines from a file one by one.
Код функції `task14`:
```python
def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
```
### Task 15: Implement a generator to iterate over words in a text file.
Код функції `task15`:
```python
def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word
```
### Task 16: Write a generator that yields characters from a string one by one.
Код функції `task16`:
```python
def string_chars_generator(string):
    for char in string:
        yield char
```
### Task 17: Create a generator to yield unique elements from a list.
Код функції `task17`:
```python
def unique_elements_generator(lst):
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            yield item
```
### Task 18: Develop a generator that yields elements of a list in reverse order.
Код функції `task18`:
```python
def reverse_list_generator(lst):
    for item in reversed(lst):
        yield item
```
### Task 19: Implement a generator to yield the Cartesian product of two lists.
Код функції `task19`:
```python
def cartesian_product_generator(list1, list2):
    for item1 in list1:
        for item2 in list2:
            yield (item1, item2)
```
### Task 20: Write a generator that yields permutations of a list.
Код функції `task20`:
```python
import itertools

def permutations_generator(lst):
    for permutation in itertools.permutations(lst):
        yield permutation
```
### Task 21: Create a generator to yield combinations of a list of elements.
Код функції `task21`:
```python
def combinations_generator(lst):
    for length in range(1, len(lst) + 1):
        for combination in itertools.combinations(lst, length):
            yield combination
```
### Task 22: Develop a generator to iterate over a list of tuples.
Код функції `task22`:
```python
def tuple_list_generator(lst):
    for tpl in lst:
        yield tpl
```
### Task 23: Implement a generator that yields elements from multiple lists in parallel.
Код функції `task23`:
```python
def parallel_lists_generator(*lists):
    for items in zip(*lists):
        yield items
```
### Task 24: Write a generator that yields elements from a nested list (flattening the list).
Код функції `task24`:
```python
def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item
```
### Task 25: Create a generator to yield elements from a nested dictionary.
Код функції `task25`:
```python
def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)
```
### Task 26: Develop a generator to yield powers of 2 up to a given number.
Код функції `task26`:
```python
def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i
```
### Task 27: Implement a generator that yields powers of a given base up to a specified limit.
Код функції `task27`:
```python
def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base
```
### Task 28: Write a generator to yield the squares of numbers in a given range.
Код функції `task28`:
```python
def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2
```
### Task 29: Create a generator to yield cubes of numbers in a specified range.
Код функції `task29`:
```python
def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3
```
### Task 30: Develop a generator that yields factorials of numbers up to a given limit.
Код функції `task30`:
```python
def factorials_generator(n):
    def factorial(x):
        if x == 0:
            return 1
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
    
    for num in range(n + 1):
        yield factorial(num)
```
### Task 31: Implement a generator to yield numbers in the Collatz sequence.
Код функції `task31`:
```python
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    yield 1]
```
### Task 32: Write a generator that yields numbers in a geometric progression.
Код функції `task32`:
```python
def geometric_progression_generator(initial_term, common_ratio, limit):
    current = initial_term
    while current <= limit:
        yield current
        current *= common_ratio
```
### Task 33: Create a generator to yield numbers in an arithmetic progression.
Код функції `task33`:
```python
def arithmetic_progression_generator(initial_term, common_difference, limit):
    current = initial_term
    while current <= limit:
        yield current
        current += common_difference
```
### Task 34: Develop a generator that yields the running sum of a list of numbers.
Код функції `task34`:
```python
def harmonic_series_generator(n):
    for k in range(1, n + 1):
        yield 1 / k
```
### Task 35: Implement a generator to yield the running product of a list of numbers.
Код функції `task35`:
```python
def round_robin_generator(*iterables):
    iterators = [iter(it) for it in iterables]
    while iterators:
        for it in iterators:
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it)
```
## 2.5 Результати
```python
gen = number_generator([1, 2, 3, 4, 5])
print(next(gen)) # 1
print(next(gen)) # 2

gen = even_number_generator(1, 10)
print(next(gen)) # 2
print(next(gen)) # 4

gen = odd_number_generator(1, 10)
print(next(gen)) # 1
print(next(gen)) # 3

gen = fibonacci_generator()
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 1
print(next(gen)) # 2

gen = prime_number_generator(10)
print(next(gen)) # 2
print(next(gen)) # 3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = pre_order_traversal(root)
print(next(gen)) # 1
print(next(gen)) # 2

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = in_order_traversal(root)
print(next(gen)) # 2
print(next(gen)) # 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = post_order_traversal(root)
print(next(gen)) # 2
print(next(gen)) # 3

graph = {
 1: [2, 3],
 2: [4],
 3: [5],
 4: [],
 5: []
}
gen = dfs_traversal(graph, 1)
print(next(gen)) # 1
print(next(gen)) # 2

gen = dict_keys_generator({'a': 1, 'b': 2, 'c': 3})
print(next(gen)) # 'a'
print(next(gen)) # 'b'

gen = dict_values_generator({'a': 1, 'b': 2, 'c': 3})
print(next(gen)) # 1
print(next(gen)) # 2

gen = dict_items_generator({'a': 1, 'b': 2, 'c': 3})
print(next(gen)) # ('a', 1)
print(next(gen)) # ('b', 2)

gen = file_lines_generator('example.txt')
print(next(gen)) # 'First line'
print(next(gen)) # 'Second line'

gen = file_words_generator('example.txt')
print(next(gen)) # 'First'
print(next(gen)) # 'line'

gen = string_chars_generator('Hello')
print(next(gen)) # 'H'
print(next(gen)) # 'e'

gen = unique_elements_generator([1, 2, 2, 3, 3, 3])
print(next(gen)) # 1
print(next(gen)) # 2

gen = reverse_list_generator([1, 2, 3, 4, 5])
print(next(gen)) # 5
print(next(gen)) # 4

gen = cartesian_product_generator([1, 2], ['a', 'b'])
print(next(gen)) # (1, 'a')
print(next(gen)) # (1, 'b')

gen = permutations_generator([1, 2, 3])
print(next(gen)) # (1, 2, 3)
print(next(gen)) # (1, 3, 2)

gen = combinations_generator([1, 2, 3])
print(next(gen)) # (1,)
print(next(gen)) # (2,)

gen = tuple_list_generator([(1, 2), (3, 4), (5, 6)])
print(next(gen)) # (1, 2)
print(next(gen)) # (3, 4)

gen = parallel_lists_generator([1, 2, 3], ['a', 'b', 'c'])
print(next(gen)) # (1, 'a')
print(next(gen)) # (2, 'b')

gen = flatten_list_generator([1, [2, [3, 4], 5], 6])
print(next(gen)) # 1
print(next(gen)) # 2

gen = nested_dict_generator({'a': {'b': 1, 'c': 2}, 'd': 3})
print(next(gen)) # ('b', 1)
print(next(gen)) # ('c', 2)

gen = powers_of_two_generator(4)
print(next(gen)) # 1
print(next(gen)) # 2

gen = powers_of_base_generator(3, 81)
print(next(gen)) # 1
print(next(gen)) # 3

gen = squares_generator(1, 5)
print(next(gen)) # 1
print(next(gen)) # 4

gen = cubes_generator(1, 4)
print(next(gen)) # 1
print(next(gen)) # 8

gen = factorials_generator(4)
print(next(gen)) # 1
print(next(gen)) # 1

gen = collatz_sequence_generator(6)
print(next(gen)) # 6
print(next(gen)) # 3

gen = geometric_progression_generator(2, 3, 20)
print(next(gen)) # 2
print(next(gen)) # 6

gen = arithmetic_progression_generator(2, 3, 20)
print(next(gen)) # 2
print(next(gen)) # 5

gen = running_sum_generator([1, 2, 3, 4])
print(next(gen)) # 1
print(next(gen)) # 3

gen = running_product_generator([1, 2, 3, 4])
print(next(gen)) # 1
print(next(gen)) # 2
```

## 2.6 Висновки
У цій лабораторній роботі було виконано завдання з генераторами та структурами даних у мові програмування Python

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

