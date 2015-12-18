# Implementing a stack with a singly linked list


class Empty(Exception):
    pass


class LinkedStack:
    '''LIFO Stack implementation using a singly linked list.'''

    class _Node:
        '''Light-weight, non-public class for storing
        linked node.'''

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        '''Create an empty stack'''
        self._head = None
        self._size = 0

    def __len__(self):
        '''Returns the number of elements in the stack'''
        return self._size

    def is_empty(self):
        '''Return True if the stack is empty'''
        return self._size == 0

    def push(self, e):
        '''Add element e to the top of the stack'''
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        '''Return (but do not remove) the element at
        the top the stack.

        Raise empty exception if the stack is empty'''

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        '''Remove and return the element from the top
        of the stack.

        Raise Empty exception if the stack is empty
        '''

        if self.is_empty():
            raise Empty('Stack is empty')
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        return e

# Implementing a queue with a SLL


class LinkedQueue:
	'''FIFO queue implementation using a singly linked list
	for storage'''

	class _Node:
        '''Light-weight, non-public class for storing
        linked node.'''

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
    	'''Create an empty queue'''
    	self._head = None
    	self._tail = None
    	self._size = 0

    def __len__(self):
    	'''Return the number of elements in the queue'''
    	return self._size

    def is_empty(self):
    	'''Return True if the queue is empty'''
    	return self._size == 0

    def first(self):
    	'''Return (but do not remove) the element at the front
    	of the queue'''
    	if self.is_empty():
    		raise Empty('Queue is empty')
    	return self._head._element

    def dequeue(self):
    	'''Remove and return the first element of the queue

    	Raise Empty exception if the queue is empty
    	'''
    	if self.is_empty():
    		raise Empty('Queue is empty')
    	e = self._head._next
    	self._size -= 1
    	if self.is_empty():
    		self._tail = None
    	return e

    def enqueue(self, e):
    	'''Add an element to the back of the queue'''
    	newest = self._Node(e, None)
    	if self.is_empty():
    		self._head = newest
    	else:
    		self.tail._next = newest
    	self._tail = newest
    	self._size += 1
