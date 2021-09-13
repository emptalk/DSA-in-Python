class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

# recursive
# time: O(h)
# aux space: O(h)
def search(root, x):
	if root == NULL:
		return False
	else if root.key == x:
		return True
	else if root.key > x:
		return search(root.left, x)
	else:
		return search(root.right, x)

# iterative
# time: O(h)
# aux space: O(1)
def search2(root, x):
	while root != None:
		if root.key == x:
			return True
		else if root.key < x:
			root = root.right
		else:
			root = root.left
	return False

