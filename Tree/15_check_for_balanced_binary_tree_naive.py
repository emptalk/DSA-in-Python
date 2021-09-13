class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
# time complexity O(n)
# auxility space O(h)
def height(root):
    if root == None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

# Naive Solution O(n^2)
def isBalanced(root):
    if root == None:
        return True
    
    lh = height(root.left)
    rh = height(root.right)
    
    return abs(lh-rh) <= 1 and \
            isBalanced(root.left) and \
            isBalanced(root.right)
            
print('isBalanced: ', isBalanced(root))            