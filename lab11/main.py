def task1(arr):
    return sum(number**2 for number in arr)

def task2(arr):
    avg = sum(arr)/len(arr)
    return sum(number for number in arr if number >= avg)

from collections import Counter

def task3(arr):
    count = Counter(arr)
    
    sorted_arr = sorted(arr, key=lambda x: (-count[x], x))
    
    return sorted_arr


def task4(arr):
    for i in range(1, arr[-1]):
        if not i in arr:
            return i
        
def task5(arr):
    arr.sort()
    
    longest_streak = 1
    current_streak = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current_streak += 1
        elif arr[i] != arr[i - 1]:
            current_streak = 1
        
        longest_streak = max(longest_streak, current_streak)
    
    return longest_streak

def task6(arr, k):
    if not arr:
        return arr
    k %= len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    return arr

def task7(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    
    products = [left_products[i] * right_products[i] for i in range(n)]
    
    return products

# Task 8: Maximum Subarray Sum
def task8(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# Task 9: Spiral Order Matrix
def task9(matrix):
    if not matrix:
        return []
    result = []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Task 10: K Closest Points to Origin
import heapq
def task10(points, k):
    if not points or k <= 0:
        return []
    heap = []
    for point in points:
        distance = point[0] ** 2 + point[1] ** 2
        heapq.heappush(heap, (distance, point))
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    return result
points = [(1, 3), (-2, 2), (5, 8), (-1, 0), (0, 0), (3, 4)]
k = 3
