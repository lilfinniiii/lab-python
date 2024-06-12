def task1(a, b, c):
    return max(a, b, c)
def task2(list):
    return sum(list)
import math
def task3(list):
    return math.prod(list)
def task4(str):
    return str[::-1]
def task5(n):
    return math.factorial(n)
def task6(n):
    return 25 <= n <= 50
def task7(text):
    return sum(map(str.isupper, text)), sum(map(str.islower, text))
def task8(orlist):
    return list(set(orlist))
def task9(list):
    return [num for num in list if num % 2 == 0]
def task10(row_num):
    def generate_pascals_row(n):
        row = [1]
        for _ in range(1, n):
            row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
        return row

    row = generate_pascals_row(row_num)
    return max(row)

print(task10(10))  # Очікуваний результат: [2, 4, 6, 8]

