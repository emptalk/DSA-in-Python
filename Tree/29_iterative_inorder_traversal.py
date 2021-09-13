from collections import deque

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def iterativeInorder(root):
	s = deque()
	curr = root

	# while curr is valid or stack is not empty	
	while curr != None or s:
		while curr != None:
			s.append(curr)
			curr = curr.left

		curr = s.pop()
		print(curr.key, end=' ')
		curr = curr.right

root = Node(10)					
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

iterativeInorder(root)