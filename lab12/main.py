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
    def sum_of_rows(self):
        sum_rows = []
        for row in self.data:
            sum_row = sum(row)
            sum_rows.append(sum_row)
        return sum_rows
    def transpose(self):
        transposed_matrix = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                transposed_matrix.data[j][i] = self.data[i][j]
        
        return transposed_matrix
    
    def multiply_by(self, other):
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

        result = Matrix(self.rows, other.columns)

        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result
    
    def is_symmetric(self):
        if self.rows != self.cols:
            return False

        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.data[i][j] != self.data[j][i]:
                    return False

        return True
    
    def rotate_right(self):
        # Transpose the matrix
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]

        # Reverse the order of elements in each row
        for row in transposed_data:
            row.reverse()

        self.data = transposed_data
    
    def flatten(self):
        flattened_matrix = [element for row in self.data for element in row]
        return flattened_matrix
    
    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        cols = len(list_of_lists[0]) if list_of_lists else 0
        matrix = Matrix(rows, cols)
        for i, row in enumerate(list_of_lists):
            for j, value in enumerate(row):
                matrix.add_element(i, j, value)
        return matrix
    
def diagonal(self):
        if self.rows != self.cols:
            raise ValueError("Matrix must be square to extract diagonal")

        diagonal_values = [self.data[i][i] for i in range(self.rows)]
        return diagonal_values


