# Лабораторна робота №15: Overview of Big Data Technologies

## 2.2 Мета роботи
Метою лабораторної роботи є виконання завдань з використанням великих даних у мові програмування Python.

## 2.3 Опис завдання

### Task 1: Clean Data
Write a function clean_data() that takes a long string of data points separated by commas, and uses map() to return a list of data points where each is stripped of whitespace and converted to lowercase.

### Task 2: Filter Emails
Create a function filter_emails() that takes a long string containing emails, and uses filter() to return a list containing only valid email addresses. An email is valid if it contains exactly one '@' symbol.

### Task 3: Extract Keywords
Write a function extract_keywords() that takes a long string of words, and uses filter() to return a list containing words that are longer than a specified length.

### Task 4: Process Text Data
Write a function process_text() that takes a long string of text data, uses map() to strip whitespace, remove special characters, and convert to lowercase, then uses filter() to return a list excluding any empty or very short entries.

### Task 5: Normalize Data
Write a function normalize_data() that takes a long string of numeric values separated by commas and normalizes them to a range between 0 and 1 based on the maximum value.

### Task 6: Concatenate Strings
Develop a function concatenate_strings() that takes multiple strings separated by a special character and concatenates them into a single string without the separator.

### Task 7: Sum Numeric Strings
Create a function sum_numeric_strings() that takes a string containing numbers separated by commas and calculates their total sum.

### Task 8: Filter Numbers
Write a function filter_numbers() that filters out numbers from a string that are above a specified threshold.

### Task 9: Map to Squares
Create a function map_to_squares() that takes a string of numbers, converts them to their squares, and returns them as a list.

### Task 10: Reverse Strings
Develop a function reverse_strings() that takes a string of words separated by commas and reverses each word.

## 2.4 Виконання роботи
### Task 1: Clean Data
Код функції `task1`:
```python
def clean_data(data):
    return list(map(lambda x: x.strip().lower(), data.split(',')))
```
### Task 2: Filter Emails
Код функції `task2`:
```python
def filter_emails(data):
    emails = data.split()
    def is_valid_email(email):
        return email.count('@') == 1
    valid_emails = filter(is_valid_email, emails)
    return list(valid_emails)
```
### Task 3: Extract Keywords
Код функції `task3`:
```python
def extract_keywords(data, num):
    words = data.split()
    def is_valid_word(word):
        return len(word) > 4
    valid_word = filter(is_valid_word, words)
    return list(valid_word)
```
### Task 4: Process Text Data
Код функції `task4`:
```python
import re

def process_text(texts):
    def clean_text(text):
        cleaned = re.sub(r'[^\w\s]', '', text).strip().lower()
        return cleaned

    text_list = texts.split(',')

    cleaned_texts = map(clean_text, text_list)

    filtered_texts = filter(lambda x: len(x) > 1, cleaned_texts)

    return list(filtered_texts)
```
### Task 5: Normalize Data
Код функції `task5`:
```python
def normalize_data(numbers):
    num_list = list(map(float, numbers.split(',')))
    
    max_value = max(num_list)
    
    normalized_numbers = list(map(lambda x: round(x / max_value, 3), num_list))
    
    return normalized_numbers
```
### Task 6: Concatenate Strings
Код функції `task6`:
```python
def concatenate_strings(data, separator):
    parts = data.split(separator)
    
    concatenated = ''.join(parts)
    
    return concatenated
```
### Task 7: Sum Numeric Strings
Код функції `task7`:
```python
def sum_numeric_strings(numbers):
    total_sum = 0
    
    number_list = numbers.split(',')
    
    for num_str in number_list:
        try:
            num = int(num_str.strip())  
            total_sum += num  
        except ValueError:
            pass  
    
    return total_sum
```
### Task 8: Filter Numbers
Код функції `task8`:
```python
def filter_numbers(numbers, threshold):
    filtered_numbers = []
    
    number_list = numbers.split()

    for num_str in number_list:
        try:
            num = float(num_str)
            if num > threshold:
                filtered_numbers.append(num)
        except ValueError:
            pass 
    
    return filtered_numbers
```
### Task 9: Map to Squares
Код функції `task9`:
```python
def map_to_squares(numbers):
    number_list = numbers.split(',')

    squared_numbers = [int(num.strip()) ** 2 for num in number_list]
    
    return squared_numbers
```
### Task 10: Reverse Strings
Код функції `task10`:
```python
def reverse_strings(words):
    word_list = words.split(',')
    
    reversed_words = [word[::-1] for word in word_list]
    
    return reversed_words
```
## 2.5 Результати
```python
data = " Apple, Banana , orange "
cleaned = clean_data(data)
print(cleaned) # ['apple', 'banana', 'orange']

emails = "mail us test@example.com and invalid-email.com.djwd
with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails) # ['test@example.com', 'example@test.co']

words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words) # ['apple', 'banana']

texts = " Hello! , Yes? , No. , "
processed_texts = process_text(texts)
print(processed_texts) # ['hello', 'yes', 'no']

numbers = "10, 20,30"
normalized_numbers = normalize_data(numbers)
print(normalized_numbers) # [0.333, 0.667, 1.0]

data = "hello*world*again"
concatenated = concatenate_strings(data, '*')
print(concatenated) # 'helloworldagain'

numbers = "1, 2, test, 3, 4"
total_sum = sum_numeric_strings(numbers)
print(total_sum) # 10

numbers = "10 test30 40"
filtered = filter_numbers(numbers, 25)
print(filtered) # [30, 40]

numbers = "1, 2, 3, 4"
squared_numbers = map_to_squares(numbers)
print(squared_numbers) # [1, 4, 9, 16]

words = "apple,banana,carrot"
reversed_words = reverse_strings(words)
print(reversed_words) # ['elppa', 'ananab', 'torrac']
```

## 2.6 Висновки
У цій лабораторній роботі було виконано завдання з використанням великих даних у мові програмування Python

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

