'''
Graph representation

(a) Adjacency Lists
'''

a, b, c, d, e, f, g, h = range(8)

# using sets
N = [
    {b, c, d, e, f},  # a
    {c, e},  # b
    {d},  # c
    {e},  # d
    {f},  # e
    {c, g, h},  # f
    {f, h},  # g
    {f, g}  # h
]

# using lists
Nl = [
    [b, c, d, e, f],  # a
    [c, e],  # b
    [d],  # c
    [e],  # d
    [f],  # e
    [c, g, h],  # f
    [f, h],  # g
    [f, g]  # h
]

# adjacency dicts with Edge Weights

Nd = [
    {b: 2, c: 1, d: 3, e: 9, f: 4},  # a
    {c: 4, e: 3},  # b
    {d: 8},  # c
    {e: 7},  # d
    {f: 5},  # e
    {c: 2, g: 2, h: 2},  # f
    {f: 1, h: 6},  # g
    {f: 9, g: 8}  # h
]

# neighborhood membership
b in Nd[a]

# Degree,
len(Nd[f])

# Edge-weight for (a, b)
N[a][b]

'''
(b) Adjacency Matrices
'''


# 	 a, b, c, d, e, f, g, h

Nm = [
    [0, 1, 1, 1, 1, 1, 0, 0],  # a
    [0, 0, 1, 0, 1, 0, 0, 0],  # b
    [0, 0, 0, 1, 0, 0, 0, 0],  # c
    [0, 0, 0, 0, 1, 0, 0, 0],  # d
    [0, 0, 0, 0, 0, 1, 0, 0],  # e
    [0, 0, 1, 0, 0, 0, 1, 1],  # f
    [0, 0, 0, 0, 0, 1, 0, 1],  # g
    [0, 0, 0, 0, 0, 1, 1, 0]  # h
]

# neighborhood membership
Nm[a][b]

# degree
sum(N[f])

# a weight matrix with infinite weight for missing edges

inf = float('inf')

# 	 a, b, c, d, e, f, g, h
Nw = [
    [0, 2, 1, 3, 9, 4, inf, inf],  # a
    [inf, 0, 4, inf, 3, inf, inf, inf],  # b
    [inf, inf, 0, 8, inf, inf, inf, inf],  # c
    [inf, inf, inf, 0, 7, inf, inf, inf],  # d
    [inf, inf, inf, inf, 0, 5, inf, inf],  # e
    [inf, inf, 2, inf, inf, 0, 2, 2],  # f
    [inf, inf, inf, inf, inf, 1, 0, 6],  # g
    [inf, inf, inf, inf, inf, 9, 8, 0]  # h
]

# neighborhood membership
Nw[a][b] < inf

# degree
sum(1 for n in Nw[a] if n < inf) - 1

'''
Implementing Trees
'''

# sample tree representation

T = [['a', 'b'], ['c'], ['d', ['e', 'f']]]

# A binary tree class


class Tree:

    def __init__(self, left, right):
        self.left = left
        self.right = right

# usage
t = Tree(Tree('a', 'b'), Tree('c', 'd'))

t.right.left

# Multiway Tree Class


class Tree:

    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next

# The Bunch pattern


class Bunch(dict):

    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self

T = Bunch

t = T(left=T(left='a', right='b'), right=T(left='c'))

t.left
# {'right': 'b', 'left': 'a'}
