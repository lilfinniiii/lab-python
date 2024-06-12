def task1(str):
    num = len(str)
    return num

def task2(n1, opr, n2):
    if opr == '+':
        num = n1 + n2
        return num
    elif opr == '-':
        num = n1 - n2
        return num
    elif opr == '/':
        num = n1 / n2
        return num
    elif opr == '//':
        num = n1 // n2
        return num
    elif opr == '*':
        num = n1 * n2
        return num
    elif opr == '**':
        num = n1 ** n2
        return num

def task3(lst):
    return max(lst)

