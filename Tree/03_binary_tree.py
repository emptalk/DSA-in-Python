class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

# test
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
