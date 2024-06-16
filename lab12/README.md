# Лабораторна робота №12: Матриці в Python

## 2.2 Мета роботи
Метою лабораторної роботи є виконання завдань з використанням матриць у мові програмування Python.

## 2.3 Опис завдання

### Завдання 1: Create a Matrix
Create a Python class Matrix that initializes a two-dimensional list with zeros. The constructor should accept two parameters: rows and columns, indicating the dimensions of the matrix.

### Завдання 2: Add Elements to Matrix
Extend the Matrix class by adding a method `add_element` that adds an element at a specific position (row, column).

### Завдання 3: Sum of Rows
Add a method `sum_of_rows` to the Matrix class that returns a list of sums of each row in the matrix.

### Завдання 4: Matrix Transposition
Create a method `transpose` in the Matrix class that returns a new Matrix object, which is the transpose of the original matrix.

### Завдання 5: Multiply Matrices
Implement a method `multiply_by` in the Matrix class that accepts another Matrix object and returns a new Matrix object that is the result of the multiplication of the two matrices.

### Завдання 6: Check Symmetric Matrix
Add a method `is_symmetric` to the Matrix class that checks if the matrix is symmetric (i.e., the matrix is equal to its transpose).

### Завдання 7: Rotate Matrix
Implement a method `rotate_right` in the Matrix class that rotates the matrix 90 degrees to the right.

### Завдання 8: Flatten Matrix
Create a method `flatten` in the Matrix class that returns a single list containingall elements of the matrix.

### Завдання 9: Matrix from List
Add a static method `from_list` to the Matrix class that creates a matrix object from a given list of lists.

### Завдання 10: Extract Diagonal
Create a method `diagonal` in the Matrix class that extracts the diagonal of a square matrix as a list.

## 2.4 Виконання роботи
### Завдання 1: Create a Matrix
Код функції `task1`:
```python
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]
```
### Завдання 2: Add Elements to Matrix
Код функції `task2`:
```python
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]
    def add_element(self, row, column, element):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = element
        else:
            raise IndexError("Index out of range")
```
### Завдання 3: Sum of Rows
Код функції `task3`:
```python
    def sum_of_rows(self):
        sum_rows = []
        for row in self.data:
            sum_row = sum(row)
            sum_rows.append(sum_row)
        return sum_rows
```
### Завдання 4: Matrix Transposition
Код функції `task4`:
```python
    def transpose(self):
        transposed_matrix = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                transposed_matrix.data[j][i] = self.data[i][j]        
        return transposed_matrix
```
### Завдання 5: Multiply Matrices
Код функції `task5`:
```python
    def multiply_by(self, other):
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

        result = Matrix(self.rows, other.columns)

        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result
```
### Завдання 6: Check Symmetric Matrix
Код функції `task6`:
```python
    def is_symmetric(self):
        if self.rows != self.cols:
            return False

        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.data[i][j] != self.data[j][i]:
                    return False

        return True
```
### Завдання 7: Rotate Matrix
Код функції `task7`:
```python
    def rotate_right(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]

        for row in transposed_data:
            row.reverse()

        self.data = transposed_data
```
### Завдання 8: Flatten Matrix
Код функції `task8`:
```python
    def flatten(self):
        flattened_matrix = [element for row in self.data for element in row]
        return flattened_matrix
```
### Завдання 9: Matrix from List
Код функції `task9`:
```python
    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        cols = len(list_of_lists[0]) if list_of_lists else 0
        matrix = Matrix(rows, cols)
        for i, row in enumerate(list_of_lists):
            for j, value in enumerate(row):
                matrix.add_element(i, j, value)
        return matrix
```
### Завдання 10: Extract Diagonal
Код функції `task10`:
```python
    def diagonal(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square to extract diagonal")

        diagonal_values = [self.data[i][i] for i in range(self.rows)]
        return diagonal_values
```
## 2.5 Результати
```python
matrix = Matrix(2, 3)
print(matrix.data) # [[0, 0, 0], [0, 0, 0]]
matrix.add_element(1, 2, 10)
print(matrix.data) # [[0, 0, 10], [0, 0, 0]]

matrix = Matrix(2, 3)
matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
matrix.add_element(1, 2, 20)
print(matrix.sum_of_rows()) # [15, 20]

matrix = Matrix(2, 3)
matrix.add_element(0, 1, 1)
matrix.add_element(1, 2, 2)
transposed = matrix.transpose()
print(transposed.data) # [[0, 0], [1, 0], [0, 2]

matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)
matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)
result = matrix1.multiply_by(matrix2)
print(result.data) # [[14, 0], [0, 0]]

matrix = Matrix(2, 2)
matrix.add_element(0, 1, 5)
matrix.add_element(1, 0, 5)
print(matrix.is_symmetric()) # True

matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
matrix.rotate_right()
print(matrix.data) # [[3, 1], [4, 2]]

matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
print(matrix.flatten()) # [1, 2, 3, 4]

list_of_lists = [[1, 2], [3, 4]]
matrix = Matrix.from_list(list_of_lists)
print(matrix.data) # [[1, 2], [3, 4]]

matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(1, 1, 2)
matrix.add_element(2, 2, 3)
print(matrix.diagonal()) # [1, 2, 3]
```

## 2.6 Висновки
У цій лабораторній роботі було виконано завдання з використанням матриць у мові програмування Python

## 2.7 Інструкції з запуску
Для запуску програми вам потрібен Python версії 3.12. Код можна запускати у будь-якому середовищі розробки або з командного рядка.

