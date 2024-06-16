def check_truth(a, b, c):
    return (a and b) or c

def logical_equivalence(p, q):
    return p == q

def xor(a, b):
    return (a and not b) or (not a and b)

def greet(is_hello):
    if is_hello:
        return "Hello, World!"
    else:
        return "Goodbye, World!"

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and x != z and y != z:
        return "All different"
    else:
        return "Neither"

def count_true(boolean_list):
    count = 0
    for value in boolean_list:
        if value:
            count += 1
    return count

def parity(num):
    binary_representation = bin(num)[2:]
    count_ones = binary_representation.count('1')
    return count_ones % 2 != 0

def majority_vote(a, b, c):
    count_true = sum([a, b, c])
    return count_true > 1

def switch(boolean_value):
    return not boolean_value

def ternary_check(condition, if_true, if_false):
    return if_true if condition else if_false

def validate(x, y, z):
    return x or (y and z)

def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

def filter_true(boolean_list):
    return [value for value in boolean_list if value]

def multiplexer(a, b, c, num):
    result = num
    if a:
        result *= 2
    if b:
        result *= 3
    if c:
        result -= 5
    return result

