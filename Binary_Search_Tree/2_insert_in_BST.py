class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

# recursive
def insert(root, x):
	if root == None:
		return Node(x)
	elif root.key < x:
		root.right = insert(root.right, x)
	elif root.key > x:
		root.left = insert(root.left, x)

	return root

# iterative
def insert2(root, x):	
	parent = None
	curr = root

	while curr != None:
		parent = curr
		if curr.key > x:
			curr = curr.left
		else if curr.key < x:
			curr = curr.right
		else:
			# x already exists
			return root 

	# parent will be parent of temp
	temp = Node(x)
	if parent == None:
		return temp
	if parent.key > x:
		parent.left = temp
	else:
		parent.right = temp
	
	return root


