class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

# O(n)
# if root is balanced,  return height
# else                  return -1
# if isBalanced(root) != -1: # if balanced
def isBalanced(root):
    if root == None:
        return 0
    
    # if any subtrees are not balanced, root is not balanced
    lh = isBalanced(root.left)
    if lh == -1:
        return -1
    rh = isBalanced(root.right)
    if rh == -1:
        return -1
    
    # When both subtrees are balanced,
    # It is easy to check if root is also balanced
    if abs(lh-rh) > 1:
        return -1
    else:
        return max(lh, rh) + 1
                
print('isBalanced: ', isBalanced(root))            