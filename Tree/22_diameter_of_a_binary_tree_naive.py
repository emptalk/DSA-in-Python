class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

# time complexity: Theta(n), this can be optimized by precompute height of every nodes
# and store it in a hash map
def height(root):
    if root == None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

# time complexity: Theta(n^2)        
def diameter(root):
    if root == None:
        return 0
        
    d1 = 1 + height(root.left) + height(root.right)
    d2 = diameter(root.left)
    d3 = diameter(root.right)
    return max(d1, d2, d3)
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(60)
root.right.left.left = Node(50)
root.right.right.right = Node(70)

print(diameter(root))