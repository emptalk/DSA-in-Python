from collections import deque

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def iterativePreorder(root):
	if root == None:
		return

	s = deque()
	s.append(root)
	while s:
		curr = s.pop()
		print(curr.key, end=' ')

		# push right first, so that we can pop left first
		if curr.right != None:
			s.append(curr.right)
		if curr.left != None:
			s.append(curr.left)

def iterativePreorder_spaceoptimized(root):
	if root == None:
		return

	s = deque()
	curr = root

	# collaborate curr and stack
	while curr != None or s:
		while curr != None:
			print(curr.key, end=' ')
			if curr.right != None:
				s.append(curr.right)
			curr = curr.left
		
		# curr is None at this line
		if s:
			curr = s.pop()


root = Node(10)					
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

iterativePreorder(root)
print()
iterativePreorder_spaceoptimized(root)