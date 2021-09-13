class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
# In this method, we assume that the keys n1 and n2 are present in Binary Tree        
def lca(root, n1, n2):
    if root == None:
        return None
    
    if root.key == n1 or root.key == n2:
        return root
    
    lca1 = lca(root.left, n1, n2)
    lca2 = lca(root.right, n1, n2)
    
    if lca1 != None and lca2 != None:
        return root
    
    if lca1 != None:
        return lca1
    else:
        return lca2
                

    
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