
# Recursively sum a sequence


def S(seq, i=0):
    if i == len(seq):
        return 0
    return S(seq, i + 1) + seq[i]

'''
General form of Recurrence

T(n) = a.T(g(n)) + f(n)

Where:
    - a: represents the number of recursive calls
    - g(n): the size of each sub-problem
    - f(n): any extra work done in the function

'''

# More examples


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# Binary Search


def binary_search(data, target, start, end):
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, start, mid - 1)
        return binary_search(data, target, mid + 1, end)


a = [20, 30, 50, 60, 89, 93, 100, 120, 150]

print(binary_search(a, 93, 0, len(a) - 1))
