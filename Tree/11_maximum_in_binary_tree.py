import sys

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
# time complixity: O(n)
# aux space: O(h)        
def getMax(root):
    if root == None:
        return -sys.maxsize - 1 # min value
    else:
        return max(root.key, getMax(root.left), getMax(root.right))
        
root = Node(10)
root.left = Node(15)
root.right = Node(20)
root.left.left = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
root.right.left.left = Node(60)
root.right.left.right = Node(70)

print(getMax(root))