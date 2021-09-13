class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(70)
root.right.right.right = Node(80)

# time complexity: theta(n)
# auxility space: O(h)
def printKDist(root, k):
    if root == None:
        return
    
    if k == 0:
        print(root.key, end=' ')
    else:
        printKDist(root.left, k - 1)
        printKDist(root.right, k - 1)

printKDist(root, 2)
