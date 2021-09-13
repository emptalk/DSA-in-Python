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

	def decreaseKey(i, x):
		arr[i] = x
		# if parent is bigger swap
		while i != 0 and arr[parent(i)] > arr[i]:
			swap(arr, i, parent(i))
			i = parent(i) # update i

	# decreaseKey(i, -INF)
	# extract min
	def deleteKey(i):

	def buildHeap():
		# do minHeapify from parent of last child to root
		i = parent(size-1) 
		while i >= 0:
			minHeapify(i)
			i -= 1
