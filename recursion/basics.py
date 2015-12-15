
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

print "Factorial: ", factorial(5)

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

print "Binary Search: ", binary_search(a, 93, 0, len(a) - 1)

# Liner Recursion


def linear_sum(S, n):
    ''' Return the sum of the first n numbers
    of sequence S.
    '''
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]

print "Linear Sum:", linear_sum(a, 4)

# Reversing a sequence with recursion


def reverse(S, start, stop):
    ''' Reverse elements in implicit slice
    S[start:stop].
    '''
    if start < stop:
        S[start], S[stop] = S[stop], S[start]
        reverse(S, start + 1, stop - 1)

    return S

print "Original: ", a
print "Reverse: ", reverse(a, 0, len(a) - 1)


def power(x, n):
    ''' Compute the value x**n for integer n.
    '''
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print "Power(10, 5): ", power(10, 5)

# Using repeated squaring


def power_(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

print "Power_(10, 5): ", power_(10, 5)
