def number_generator(numbers):
    for number in numbers:
        yield number

def even_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number

def odd_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_number_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value

def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))

def dict_keys_generator(dictionary):
    for key in dictionary.keys():
        yield key

def dict_values_generator(dictionary):
    for value in dictionary.values():
        yield value

def dict_items_generator(dictionary):
    for item in dictionary.items():
        yield item

def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

def string_chars_generator(string):
    for char in string:
        yield char

def unique_elements_generator(lst):
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            yield item

def reverse_list_generator(lst):
    for item in reversed(lst):
        yield item

def cartesian_product_generator(list1, list2):
    for item1 in list1:
        for item2 in list2:
            yield (item1, item2)

import itertools

def permutations_generator(lst):
    for permutation in itertools.permutations(lst):
        yield permutation

def combinations_generator(lst):
    for length in range(1, len(lst) + 1):
        for combination in itertools.combinations(lst, length):
            yield combination

def tuple_list_generator(lst):
    for tpl in lst:
        yield tpl

def parallel_lists_generator(*lists):
    for items in zip(*lists):
        yield items

def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i

def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base

def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2

def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3

def factorials_generator(n):
    def factorial(x):
        if x == 0:
            return 1
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
    
    for num in range(n + 1):
        yield factorial(num)

def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    yield 1

def geometric_progression_generator(initial_term, common_ratio, limit):
    current = initial_term
    while current <= limit:
        yield current
        current *= common_ratio

def arithmetic_progression_generator(initial_term, common_difference, limit):
    current = initial_term
    while current <= limit:
        yield current
        current += common_difference

def harmonic_series_generator(n):
    for k in range(1, n + 1):
        yield 1 / k

def round_robin_generator(*iterables):
    iterators = [iter(it) for it in iterables]
    while iterators:
        for it in iterators:
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it)
