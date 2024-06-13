def task1(numbers):
  if len(numbers) != 2:
    raise ValueError("Input tuple must contain exactly two numbers")
  return sum(numbers)

def task2(data):
  return len(data)

def task3(numbers):
  sorted_numbers = sorted(numbers, reverse=True)
  return sorted_numbers[0]

def task4(data):
  if not isinstance(data[0], dict):
    raise ValueError("Input tuple must contain a dictionary as the first element")
  return data[0].get("name")

def task5(data):
  sorted_data = [element for element in data if isinstance(element, tuple)]
  if not sorted_data:
    return None

  return sorted(sorted_data, key=lambda x: len(x[0]))[-1][-1]


def task6(data):
  even_numbers = []
  for element in data:
    even_numbers.extend([num for num in element if num % 2 == 0])
  product = 1
  for num in even_numbers:
    product *= num
  return product if product else 1

def task7(data):
  sum_of_seconds = 0
  for inner_tuple in data:
    if len(inner_tuple) != 2:
      raise ValueError("Inner tuples must contain exactly two numbers")
    sum_of_seconds += inner_tuple[1]
  return sum_of_seconds

# Завдання 1
print(task1((3, 5)))  # Очікуваний результат: 8

# Завдання 2
print(task2((1, 'a', 3, 'b', 5)))  # Очікуваний результат: 5

# Завдання 3
print(task3((3, 1, 4, 2)))  # Очікуваний результат: 4

# Завдання 4
print(task4(({'name': 'John', 'age': 30},)))  # Очікуваний результат: 'John'

# Завдання 5
data = [(('a', 'b', 'c'), 3), (('d',), 1), (('e', 'f'), 2)]
print(task5(data))  # Очікуваний результат: 3

# Завдання 6
print(task6(([1, 2, 3], [4, 5, 6])))  # Очікуваний результат: 15

# Завдання 7
print(task7(((1, 2), (3, 4), (5, 6))))  # Очікуваний результат: 12
