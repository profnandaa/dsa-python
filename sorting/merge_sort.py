class MergeSort:

    def __init__(self, listx):
        self.list = listx

    def merge(self, p, q, r):
        L = self.list[p:q + 1]
        R = self.list[q + 1:r + 1]

        # add sentinels
        L.append(float("inf"))
        R.append(float("inf"))

        i = 0
        j = 0
        for k in xrange(p, r + 1):
            if L[i] <= R[j]:
                self.list[k] = L[i]
                i += 1
            else:
                self.list[k] = R[j]
                j += 1

        return self.list

    def merge_sort(self, p, r):
        if p < r:
            q = (p + r) // 2
            self.merge_sort(p, q)
            self.merge_sort(q + 1, r)
            self.merge(p, q, r)
        return self.list

    def sort(self):
        p = 0
        r = len(self.list) - 1
        self.merge_sort(p, r)
        return self.list
