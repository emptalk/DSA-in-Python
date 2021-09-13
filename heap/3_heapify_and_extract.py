arr = None
size
capacity

# tree shape is not changed while doing minHeapify
# time: O(log n)
# aux space: O(h)
# when doing heapify, left subtree and right subtree should be already correct heap
# initially, only root can violate
def minHeapify(i): # must start from root
	lt = left(i)
	rt = right(i)
	smallest = i
	if lt < size && arr[lt] < arr[i]:
		smallest = lt
	if rt < size && arr[rt] < arr[smallest]:
		smallest = rt
	if smallest != i:
		swap(arr, i, smallest)
		minHeapify(smallest) # can change to iterative 

def swap(arr, i1, i2):
	arr[i1], arr[i2] = arr[i2], arr[i1]		

# extract: swap root with last child and heapify
def extractMin():
	if size == 0:
		return INF # INT_MAX
	if size == 1:
		size -= 1
		return arr[0]
	
	swap(arr, 0, size-1)
	size -= 1

	minHeapify(0)
	return arr[size] # return min value
