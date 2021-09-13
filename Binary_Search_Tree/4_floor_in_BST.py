class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

# time: O(h)
# aux space: O(1)
def floor(root, x):
	res = None
	while root != None:
		if root.key == x:
			return root # equal floor
		else if x < root.key:
			root = root.left
		else: # root.key < x
			root = root.right
			res = root # new potential floor which is not equal to x

	return res # not equal floor