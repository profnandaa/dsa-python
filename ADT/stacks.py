# Simple Array-based stack implementation

'''
The adapter pattern:

Using Python list class

S.push(e)	-> L.append(e)
S.pop()		-> L.pop()
S.top()		-> L[-1]
S.is_empty()-> len(L) == 0
len(S)		-> len(L)

'''


class Empty(Exception):
    '''Error attempting to access an element from
    an empty container.'''
    pass


class ArrayStack:
    '''
    LIFO Stack implementation using a Python list
    as underlying storage.
    '''

    def __init__(self):
        '''Create an empty stack.'''
        self._data = []

    def __len__(self):
        '''Return the number of elements in the stack'''
        return len(self._data)

    def is_empty(self):
        '''Return True if the stack is empty'''
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        '''Return (but do not remove) the elemet at the top
        of the stack. Raise exception if the stack is empty'''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        '''Remove and return element from the top of the list'''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

# example

a = ArrayStack()

a.push(10)
a.push(30)
a.push(40)
a.push(3)

print(a.pop())
print(a.top())
