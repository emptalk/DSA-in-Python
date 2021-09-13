class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

# time: O(h)
# aux space: O(h)
def delNode(root, x):
	if root == None:
		return None

	if root.key > x:
		root.left = delNode(root.left, x)        
	else if root.key < x:
		root.right = delNode(root.right, x)
	else: # delete root
		if root.left == None:
			return root.right
		else if root.right == None:
			return root.left
		else:
			succ = getSucc(root)
			root.key = succ.key # replace root with succ
			root.right = delNode(root.right, succ.key)
		return root

def getSucc(root):
	curr = root.right
	while curr != None and curr.left != None:
		curr = curr.left
	return curr
