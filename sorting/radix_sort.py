class RadixSort:

    def __init__(self, input_list):
        self.list = input_list

    def swap(self, x, y):
        self.list[x], self.list[y] = self.list[y], self.list[x]

    def bubble_sort(self, pos):
        for i in xrange(0, len(self.list)):
            for j in xrange(len(self.list) - 1, i, -1):
                x = list(str(self.list[j]))
                y = list(str(self.list[j - 1]))

                if x[pos] < y[pos]:
                    self.swap(j, j - 1)

        return self.list

    def sort(self, d):
        for i in xrange(d - 1, -1, -1):
            self.bubble_sort(i)
        return self.list


a = [100, 150, 500, 200, 130, 140]

b = a[:]

c = RadixSort(a)

print a
print(c.sort(3))


# print a
# print c.list
