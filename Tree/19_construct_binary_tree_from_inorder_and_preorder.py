class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
# time complexity : O(n^2)        
preIndex = 0
def cTree(inorder, preorder, instart, inend):
    global preIndex

    if instart > inend:
        return None
    
    root = Node(preorder[preIndex])
    preIndex += 1

    #find root in inorder range(instart, inend + 1)
    for i in range(instart, inend + 1): # O(n), can be optimized with hashing
        if inorder[i] == root.key:
            inIndex = i
            break
    
    root.left = cTree(inorder, preorder, instart, inIndex-1)
    root.right = cTree(inorder, preorder, inIndex+1, inend)
    return root

inorder = [20, 10, 40, 30, 50]
preorder = [10, 20, 30, 40, 50]

# construct tree from inorder and preorder
root = cTree(inorder, preorder, 0, len(inorder)-1)

# validate if root is corruct
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
        
print('inorder')
inorder(root)
print('\n')

print('preorder')        
preorder(root)