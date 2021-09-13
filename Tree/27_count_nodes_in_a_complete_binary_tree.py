class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def countNodes(root):
	if root == None:
		return 0
	else:
		return 1 + 	countNodes(root.left) + \
					countNodes(root.right)        


root = Node(10)					
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

#print(countNodes(root))

def countNodesForComplete(root):
	lh = 0
	rh = 0
	
	curr = root
	while curr != None:
		lh += 1
		curr = curr.left
	
	curr = root	
	while curr != None:
		rh += 1
		curr = curr.right

	if lh == rh:
		return pow(2, lh) - 1
	return 1 + countNodesForComplete(root.left) + \
				countNodesForComplete(root.right)

print(countNodesForComplete(root))				