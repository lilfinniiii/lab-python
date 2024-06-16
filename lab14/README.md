# Лабораторна робота №14: Логічні вирази

## 2.2 Мета роботи
Метою лабораторної роботи є виконання завдань з використанням логічних виразів у мові програмування Python.

## 2.3 Опис завдання

### Завдання 1: Basic Boolean Operations
Write a function check_truth that takes three boolean parameters ( a , b , c ) and returns the result of the expression (a and b) or c .

### Завдання 2: Logical Equivalence
Write a function logical_equivalence that takes two boolean parameeters and returns True if they are logically equivalent, otherwise False .

### Завдання 3: Exclusive Or (XOR)
Write a function xor that takes two boolean arguments and returns True if exactly one of the arguments is True .

### Завдання 4: Conditional Greeting
Write a function greet that takes a boolean value. If True , the function should return "Hello, World!", otherwise it should return "Goodbye, World!"

### Завдання 5: Nested Conditions
Write a function nested_condition that takes three integers ( x , y , z ). The function should return "All same" if all three are equal, "All different" if they are all different, and "Neither" otherwise.

### Завдання 6: Conditional Counting
Write a function count_true that accepts a list of boolean values and returns the count of how many are True .

### Завдання 7: Boolean Parity
Write a function parity that accepts an integer and returns True if the number of 1 s in the binary representation of the number is even, otherwise False .

### Завдання 8: Majority Vote
Write a function majority_vote that takes three boolean inputs and returns True if more than half of them are True , otherwise False .

### Завдання 9: Boolean Switch
Write a function switch that takes a boolean value and returns its opposite.

### Завдання 10: Ternary Operator Simulation
Write a function ternary_check that simulates a ternary operator. It takes three parameters: a boolean condition, a result if true, and a result if false. It returns the corresponding result based on the condition.

### Завдання 11: Validate Combination
Write a function validate that takes three booleans ( x , y , z ) and returns True if x is True or both y and z are True , otherwise False .

### Завдання 12: Condition Chain
Write a function chain_check that evaluates a sequence of conditions. It takes three integers and returns "Increasing" if they are in strictly increasing order, "Decreasing" if in strictly decreasing order, or "Neither" otherwise.

### Завдання 13: Boolean Filter
Write a function filter_true that takes a list of boolean values and returns anew list containing only the True values.

### Завдання 14: Conditional Multiplexer
Write a function multiplexer that takes four parameters: three boolean inputs and one integer. If the first boolean is True , return double the integer. If the second is True , return triple the integer. If the third is True , return the integer minus five. If none are True , return the integer unchanged.

## 2.4 Виконання роботи
### Завдання 1: Basic Boolean Operations
Код функції `task1`:
```python
def check_truth(a, b, c):
    return (a and b) or c
```

### Завдання 2: Logical Equivalence
Код функції `task2`:
```python
def logical_equivalence(p, q):
    return p == q
```

### Завдання 3: Exclusive Or (XOR)
Код функції `task3`:
```python
def xor(a, b):
    return (a and not b) or (not a and b)
```

### Завдання 4: Conditional Greeting
Код функції `task4`:
```python
def greet(is_hello):
    if is_hello:
        return "Hello, World!"
    else:
        return "Goodbye, World!"
```

### Завдання 5: Nested Conditions
Код функції `task5`:
```python
def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and x != z and y != z:
        return "All different"
    else:
        return "Neither"
```

### Завдання 6: Conditional Counting
Код функції `task6`:
```python
def count_true(boolean_list):
    count = 0
    for value in boolean_list:
        if value:
            count += 1
    return count
```

### Завдання 7: Boolean Parity
Код функції `task7`:
```python
def parity(num):
    binary_representation = bin(num)[2:]
    count_ones = binary_representation.count('1')
    return count_ones % 2 != 0
```

### Завдання 8: Majority Vote
Код функції `task8`:
```python
def majority_vote(a, b, c):
    count_true = sum([a, b, c])
    return count_true > 1
```
### Завдання 9: Boolean Switch
Код функції `task9`:
```python
def switch(boolean_value):
    return not boolean_value
```
### Завдання 10: Ternary Operator Simulation
Код функції `task10`:
```python
def ternary_check(condition, if_true, if_false):
    return if_true if condition else if_false
```
### Завдання 11: Validate Combination
Код функції `task11`:
```python
def validate(x, y, z):
    return x or (y and z)
```
### Завдання 12: Condition Chain
Код функції `task12`:
```python
def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"
```
### Завдання 13: Boolean Filter
Код функції `task13`:
```python
def filter_true(boolean_list):
    return [value for value in boolean_list if value]
```
### Завдання 14: Conditional Multiplexer
Код функції `task14`:
```python
def multiplexer(a, b, c, num):
    result = num
    if a:
        result *= 2
    if b:
        result *= 3
    if c:
        result -= 5
    return result
```
## 2.5 Результати
```python
print(check_truth(True, False, True)) # True
print(logical_equivalence(True, True)) # True
print(logical_equivalence(True, False)) # False
print(xor(True, False)) # True
print(xor(True, True)) # False
print(greet(True)) # Hello, World!
print(greet(False)) # Goodbye, World!
print(nested_condition(3, 3, 3)) # All same
print(nested_condition(3, 4, 5)) # All different
print(count_true([True, False, True, False, True])) # 3
print(parity(3)) # False (binary 11)
print(majority_vote(True, True, False)) # True
print(switch(True)) # False
print(ternary_check(True, "Yes", "No")) # Yes
print(validate(True, False, True)) # True
print(chain_check(1, 2, 3)) # Increasing
print(chain_check(3, 2, 1)) # Decreasing
print(filter_true([True, False, True, False])) # [True, True]
print(multiplexer(False, False, True, 10)) # 5
```

## 2.6 Висновки
У цій лабораторній роботі було виконано завдання з використанням регулярних виразів у мові програмування Python

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

