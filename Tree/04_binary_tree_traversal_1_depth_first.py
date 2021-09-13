class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

# create binary tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

# time complexity: O(n) 
# auxiliry space: O(h)
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)

def preorder(root):
    if root != None:
        print(root.key, end=' ')
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)    
        print(root.key, end=' ')

# traverse
print('inorder')        
inorder(root)
print('')        

print('preorder')        
preorder(root)
print('')        

print('postorder')        
postorder(root)
print('')        
