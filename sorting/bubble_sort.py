class BubbleSort:

    def __init__(self, input_list):
        self.list = input_list

    def swap(self, x, y):
        '''	A helper method for sort() that
                swaps items in the list
        '''
        self.list[x], self.list[y] = self.list[y], self.list[x]

    def sort(self):
        for i in xrange(0, len(self.list)):
            for j in xrange(len(self.list) - 1, i, -1):
                if self.list[j] < self.list[j - 1]:
                    self.swap(j, j - 1)
        return self.list
