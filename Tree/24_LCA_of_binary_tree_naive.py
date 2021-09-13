class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
def findPath(root, path, n):
    if root == None:
        return False
        
    path.append(root)
    
    if root.key == n:
        return True
    
    # since root is not n, try findPath with left subtree and right subtree
    if findPath(root.left, path, n) or \
        findPath(root.right, path, n):
        return True
    
    # pop root from path because findPath couldn't find n
    path.pop()
    return False
    
def lca(root, n1, n2):
    path1 = []
    path2 = []
    if findPath(root, path1, n1) == False or \
        findPath(root, path2, n2) == False:
        return None
    
    # since we have found both path we can check lca
    i = 0
    while i < len(path1)-1 and i < len(path2)-1:
        if path1[i+1] != path2[i+1]:
            return path1[i]
        i += 1
        
    return None
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

# test findPath
#p = []
#r = findPath(root, p, 50)
#
#for e in p:
#    print(e.key, end=' ')
#print()    
#print(r)
res = lca(root, 20, 50)
if res != None:
    print(res.key)
else:
    print('There is not common anscestor')