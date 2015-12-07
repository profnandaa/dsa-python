class SelectionSort:

    def __init__(self, input_list):
        self.list = input_list

    def swap(self, x, y):
    	self.list[x], self.list[y] = self.list[y], self.list[x]

    def findMin(self, pos):
    	'''
    	Finds the minimum number from position `i`
    	to the end of the list.
    	'''
    	min_index = pos
    	for i in xrange(pos+1, len(self.list)):
    		if self.list[i] < self.list[min_index]:
    			min_index = i

    	return min_index

    def sort(self):
    	for i in xrange(0, len(self.list)-1):
    		self.swap(i, self.findMin(i))

    	return self.list


