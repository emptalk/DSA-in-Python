class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

EMPTY = -1
def serialize(root, arr):
	if root == None:
		arr.append(EMPTY)
		return

	arr.append(root.key)
	serialize(root.left, arr)
	serialize(root.right, arr)

index = 0
def deserialize(arr):
	global index

	if index == len(arr):
		return None

	val = arr[index]
	index += 1

	if val == EMPTY:
		return None

	root = Node(val)
	root.left = deserialize(arr)
	root.right = deserialize(arr)

	return root


root = Node(10)					
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

arr = []
serialize(root, arr)
print(arr)

index = 0
root2 = deserialize(arr)
arr2 = []
serialize(root2, arr2)
print(arr2)

# we can create binary tree with arr as well.
