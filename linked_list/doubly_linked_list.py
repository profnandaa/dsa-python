class Empty(Exception):
    pass


class _DoublyLinkedBase:
    '''A base class providing a doubly linked list representation.'''

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        '''Create an empty list'''
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        '''Add element e between two existing nodes and
        return new node.'''
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        '''Delete nonsentinel node from the list and return
        its element.'''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class LinkedDeque(_DoublyLinkedBase):
    '''Double-ended queue implementation based on a doubly linked list'''

    def first(self):
        '''Return (but do not remove) the element at the front of the deque'''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element

    def last(self):
        '''Return (but do not remove) the element at the back of the deque'''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        '''Add an element to the front of the deque'''
        self._insert_between(e, self._header, self._header._next)

    def delete_first(self):
        '''Remove and return the element from the back of the deque

        Raise Empty exception if the deque is empty'''
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)
