
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
