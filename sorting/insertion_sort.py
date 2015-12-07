class InsertionSort:

    def __init__(self, input_list):
        self.list = input_list

    def swap(self, x, y):
        self.list[x], self.list[y] = self.list[y], self.list[x]

    def bubbleLast(self, pos):
        for i in xrange(pos, 0, -1):
            if self.list[i] < self.list[i - 1]:
                self.swap(i, i - 1)

    def sort(self):
        for i in xrange(1, len(self.list)):
            self.bubbleLast(i)

        return self.list
