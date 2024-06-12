def task1(my_list):
    my_list.insert(1, -5)
    min_element = min(my_list)
    max_element = max(my_list)
    my_list.insert(2, [1, 2, 3])
    my_list.append(["Сідєльніков", "Євген"])
    list_length = len(my_list)
    print(my_list)
    print(min_element)
    print(max_element)
    print(list_length)
    return my_list, min_element, max_element, list_length

from statistics import mean

def task2(A,B,C):
    total_cost = sum([quantity * price for quantity, price in zip(B, C)])
    average_price = mean(C)
    k = B.index(max(B))
    most_stocked_item = A[k]
    return total_cost, average_price, most_stocked_item

def task3():
    A1 = []
    A2 = []

    for i in range(-25, 25):
        if i > 0:
            A1.append(i)
        elif i < 0:
            A2.append(i)
    return A1, A2


def task4(my_string):
    count = my_string.count("a")
    return count

def task5(my_string):
    modified_str = my_string.replace("GOOD", "NICE")
    word_count = len(my_string.split())
    return modified_str, word_count

def task6():
    my_list = [1, 2, 3, 4, 5]
    total_sum = sum(my_list)
    return total_sum

def task7(my_list):
    result = []
    for num in my_list:
        if num % 7 == 0 and num % 5 == 0:
            result.append(num)
    return result

