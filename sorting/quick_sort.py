class QuickSort:

    def __init__(self, listx):
        self.list = listx

    def swap(self, x, y):
        self.list[x], self.list[y] = self.list[y], self.list[x]

    def partition(self, p, r):
        x = self.list[r]
        i = p - 1

        for j in xrange(p, r):
            if self.list[j] <= x:
                i += 1
                self.swap(i, j)
                
        self.swap(i + 1, r)

        return i + 1

    def quick_sort(self, p, r):
        if p < r:
            q = self.partition(p, r)
            self.quick_sort(p, q - 1)
            self.quick_sort(q + 1, r)

        return self.list

    def sort(self):
        p = 0
        r = len(self.list) - 1
        self.quick_sort(p, r)
        return self.list
