# Лабораторна робота №8: Робота з JSON у Python

## 2.2 Мета роботи
Метою лабораторної роботи є виконання різноманітних завдань з обробкою даних у форматі JSON у мові програмування Python.

## 2.3 Опис завдання

### Завдання 1: JSON Parsing and Data Retrieval
Parse a JSON file and return a list of names of individuals above a certain age.

### Завдання 2: Data Transformation and JSON Serialization
Transform a list of dictionaries into a JSON string and write it to a file.

### Завдання 3: JSON Schema Validation
Validate JSON files against a given schema.

### Завдання 4: Nested JSON Data Handling
Extract specific information from a complex nested JSON structure.

### Завдання 5: Updating JSON Data
Update certain fields in a JSON file based on given criteria.

## 2.4 Виконання роботи
```python
import json
import jsonschema
```
### Завдання 1: JSON Parsing and Data Retrieval
Код функції `task1`:
```python
def task1(json_file_path, age_threshold):
    names_above_age = []

    with open(json_file_path, 'r') as file:
        data = json.load(file)

        for person in data:
            if person.get('age') and person['age'] > age_threshold:
                names_above_age.append(person['name'])

    return names_above_age
```
### Завдання 2: Data Transformation and JSON Serialization
Код функції `task2`:
```python
def task2(data_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json_data = json.dumps(data_list, ensure_ascii=False, indent=4)
        file.write(json_data)

    return json_data
```
### Завдання 3: JSON Schema Validation
Код функції `task3`:
```python
def task3(schema, file_paths):
    invalid_files = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        try:
            jsonschema.validate(instance=json_data, schema=schema)
        except jsonschema.exceptions.ValidationError:
            invalid_files.append(file_path)
    return invalid_files
```
### Завдання 4: Nested JSON Data Handling
Код функції `task4`:
```python
def task4(json_data, key):
    results = []

    if isinstance(json_data, dict):
        if key in json_data:
            results.append(json_data[key])
        for k, v in json_data.items():
            results.extend(task4(v, key))
    elif isinstance(json_data, list):
        for item in json_data:
            results.extend(task4(item, key))

    return results
```
### Завдання 5: Updating JSON Data
Код функції `task5`:
```python
def task5(file_path, category, update_function):
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    for item in json_data:
        if item.get('category') == category:
            update_function(item)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)
    print("Update data:")
    print(json.dumps(json_data, indent=4))
    item['price'] += 10 

```
## 2.5 Результати
```python
# Завдання 1
# 'people.json':
# [
#     {"name": "John", "age": 30},
#     {"name": "Jane", "age": 25},
#     {"name": "Doe", "age": 35},
#     {"name": "Alice", "age": 20}
# ]

result = task1('people.json', 25)
print("Names of individuals above the age of 25:", result)
# Очікуваний результат: ['John', 'Doe', 'Alice']

# Завдання 2

people = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "Los Angeles"},
    {"name": "Doe", "age": 35, "city": "Chicago"}
]

task2(people, 'output.json')

with open('output.json', 'r') as file:
    contents = file.read()
    print("Contents of 'output.json':")
    print(contents)


# Завдання 3
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "city": {"type": "string"}
    },
    "required": ["name", "age", "city"]
}

files_to_validate = ['output.json', 'invalid_data.json']

invalid_files = task3(schema, files_to_validate)
print("Files that do not conform to the schema:")
print(invalid_files)


# Завдання 4
# 'nested_data.json'
# {
#     "person": {
#         "name": "John",
#         "details": {
#             "age": 30,
#             "address": {
#                 "city": "New York",
#                 "country": "USA"
#             }
#         }
#     }
# }

result = task4('nested_data.json', 'city')
print("Values associated with the key 'city':")
print(result)


# Завдання 5
# 'products.json
# [
#     {"name": "Product1", "category": "electronics", "price": 100},
#     {"name": "Product2", "category": "clothing", "price": 50},
#     {"name": "Product3", "category": "electronics", "price": 200}
# ]

task5('products.json', 'electronics', increase_price)
print("Products.json file updated successfully!")

```

## 2.6 Висновки
У цій лабораторній роботі ми реалізували різноманітні завдання з обробкою даних та обробкою помилок у мові програмування Python

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

