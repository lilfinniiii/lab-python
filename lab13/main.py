import re

def interpolate_missing(numbers):
    interpolated_numbers = []
    for i, num in enumerate(numbers):
        if num is None:
            left_index = i - 1
            right_index = i + 1
            
            while left_index >= 0 and numbers[left_index] is None:
                left_index -= 1
                
            while right_index < len(numbers) and numbers[right_index] is None:
                right_index += 1
                
            left = numbers[left_index] if left_index >= 0 else None
            right = numbers[right_index] if right_index < len(numbers) else None
            
            if left is not None and right is not None:
                interpolated_numbers.append(left + (right - left) / (right_index - left_index))
            elif left is not None:
                interpolated_numbers.append(left)
            elif right is not None:
                interpolated_numbers.append(right)
            else:
                interpolated_numbers.append(None)
        else:
            interpolated_numbers.append(num)
    
    return interpolated_numbers

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def process_batches(numbers, batch_size):
    max_values = []
    for i in range(0, len(numbers), batch_size):
        batch = numbers[i:i + batch_size]
        max_values.append(max(batch))
    return max_values



def encode_string(s):
    encoded = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += str(count) + s[i - 1]
            count = 1
    encoded += str(count) + s[-1]
    return encoded


def decode_string(s):
    decoded = ""
    i = 0
    while i < len(s):
        count = int(s[i])
        decoded += s[i + 1] * count
        i += 2
    return decoded


def rotate_matrix(matrix):
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]
    return rotated_matrix


def regex_search(strings, pattern):
    matching_strings = []
    for string in strings:
        if re.match(pattern, string):
            matching_strings.append(string)
    return matching_strings


def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def group_by_key(data, key):
    grouped_data = {}
    for item in data:
        if item[key] in grouped_data:
            grouped_data[item[key]].append(item['value'])
        else:
            grouped_data[item[key]] = [item['value']]
    return grouped_data


import numpy as np

def remove_outliers(lst):
    mean = np.mean(lst)
    std_dev = np.std(lst)
    outliers_removed = [x for x in lst if abs(x - mean) <= 2 * std_dev]
    return outliers_removed



