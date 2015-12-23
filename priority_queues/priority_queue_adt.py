class PriorityQueueBase:
    '''Abstract base class for priority queue.'''

    class _Item:
        '''Lightweight composition to store priority queue items.'''

        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        '''Return True if the priority queue is empty.'''
        return len(self) == 0


# Implementing with an unsorted list

class UnsortedPriorityQueue(PriorityQueueBase):
    '''A min-oriented priority queue implemented with an unsorted list.'''

    def _find_min(self):
        '''Return Position of item with minimum key.'''
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        '''Create a new empty priority queue.'''
        self._data = PositionalList()

    def __len__(self):
        '''Return the number of items in the priority queue.'''
        return len(self._data)

    def add(self, key, value):
        '''Add a key-value paire.'''
        self._data.add_last(self._Item(key, value))

    def min(self):
        '''Return but do not remove (k, v) tuple with minimum key.'''
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        '''Remove and return (k, v) tuple with minimum key.'''
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

# Implementing with a sorted list


class SortedPriorityQueue(PriorityQueueBase):
    '''A min-oriented priority queue implemented with sorted list.'''

    def __init__(self):
        '''Create a new empty Priority Queue.'''
        self._data = PositionalList()

    def __len__(self):
        '''Return the number of items in the priority queue.'''
        return len(self._data)

    def add(self, key, value):
        '''Add a key-value pair.'''
        newest = self._Item(key, value)
        walk = self._data.last()

        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        '''Return but do not remove the (k,v) tuple of minimum key.'''
        if self.is_empty():
            raise Empty('Priority queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        '''Remove and return the (k,v) tuple with minimum key.'''
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
