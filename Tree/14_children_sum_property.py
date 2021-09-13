class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
def isCSum(root):
    if root == None:
        return True    
    if root.left == None or root.right == None:
        return True
        
    sum = 0
    if root.left != None:
        sum += root.left.key
    if root.right != None:
        sum += root.right.key
        
    return root.key == sum and \
            isCSum(root.left) and \
            isCSum(root.right)
            
            
root = Node(20)
root.left = Node(8)
root.right = Node(12)
root.right.left = Node(3)
root.right.right = Node(9)

print(isCSum(root))

            