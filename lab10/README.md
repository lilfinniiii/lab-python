# Лабораторна робота №10: Класи в Python

## 2.2 Мета роботи
Метою лабораторної роботи є виконання завдань з використанням класів у мові програмування Python.

## 2.3 Опис завдання

### Завдання 1: Class Creation
Create a Python class named “Student” with the following attributes: - name - age - grade

### Завдання 2: Create Method
Add a method named display_info() to the Student class that prints the student’s name, age, and grade in the format “Name: [name], Age: [age], Grade: [grade]”.

### Завдання 3: Inheritance
Create two classes: Animal and Dog. Animal should have attributes name and sound. Add a make_sound() method to Animal that returns the string “[name]: [sound]”. Dog should inherit from Animal and have an additional attribute breed.

### Завдання 4: Polymorphism
Create a class Bird with a method fly() that returns None. Then create two subclasses: Sparrow and Penguin. Override the fly() method in Sparrow to return the string “Sparrow flies high” and in Penguin to return the string “Penguin cannot fly”.

### Завдання 5: Encapsulation
Create a class Encapsulation with the following attributes:
• public
• _private
• __protected

### Завдання 6: Rectangle
Create a Rectangle class that has width and height attributes, and a calculate_perimeter() method that returns the perimeter of the shape.

### Завдання 7: AverageCalculator
Create an AverageCalculator class that has a numbers attribute and takes a list of integers. The class should have a calculate_average() method that returns the arithmetic mean of the numbers in the list.

## 2.4 Виконання роботи
### Завдання 1: Class Creation
Код функції `task1`:
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
```
### Завдання 2: Create Method
Код функції `task2`:
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
```
### Завдання 3: Inheritance
Код функції `task3`:
```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name}: {self.sound}"

class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed
```
### Завдання 4: Polymorphism
Код функції `task4`:
```python
class Bird:
    def fly(self):
        return None

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"
```
### Завдання 5: Encapsulation
Код функції `task5`:
```python
class Encapsulation:
    def __init__(self, public, private, protected):
        self.public = public
        self._private = private
        self.__protected = protected
```
### Завдання 6: Rectangle
Код функції `task6`:
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
```
### Завдання 7: AverageCalculator
Код функції `task7`:
```python
class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)
```
## 2.5 Результати
```python
student = Student(name="Ivan", age=30, grade="2")
print(student.display_info()) # Name: Ivan, Age: 30, Grade: 2

animal = Animal(name="Lala", sound="            ")
dog = Dog(name="Lala", sound="Auuuuuuu", breed="Spitz")
print(animal.make_sound()) # Lala:
print(dog.make_sound()) # Lala: Auuuuuuu

bird = Bird()
sparrow = Sparrow()
penguin = Penguin()
print(bird.fly()) # None
print(sparrow.fly()) # Sparrow flies high
print(penguin.fly()) # Penguin cannot fly

obj = Encapsulation(1, 2, 3)
print(obj.public) # 1
print(obj._private) # 2
print(obj._Encapsulation__protected) # 3
print(obj.__protected) # AttributeError

rectangle = Rectangle(width=5, height=4)
print(rectangle.calculate_perimeter()) # 18

numbers = [5, 10, 15, 20]
avg_calculator = AverageCalculator(numbers)
print(avg_calculator.calculate_average()) # Expected output: 12.5
```

## 2.6 Висновки
У цій лабораторній роботі було виконано завдання з використанням класів у мові програмування Python

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

