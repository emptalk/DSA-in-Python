class minHeap:
	def __init__(self, c):
		self.arr = [None for _ in range(c)]
		self.size = 0
		self.capacity = c

	def left(self, i):
		return 2*i + 1
	def right(self, i):
		return 2*i + 2
	def parent(self, i):
		return int((i-1)/2)

	def insert(self, x):
		if self.size == self.capacity: # full
			return
		self.size += 1
		arr[size-1] = x
		
		i = size-1
		while i != 0 and arr[parent(i)] > arr[i]:
			swap(arr, i, parent(i))
			i = parent(i)

def swap(arr, i1, i2):
	arr[i1], arr[i2] = arr[i2], arr[i1]
