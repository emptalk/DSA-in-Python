class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

diameter = 0

def height(root):    
    if root == None:
        return 0
        
    lh = height(root.left)
    rh = height(root.right)
    
    # update diameter while solving height
    global diameter
    diameter = max(diameter, 1 + lh + rh)
    
    return 1 + max(lh, rh)
        
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(60)
root.right.left.left = Node(50)
root.right.right.right = Node(70)

# time complexity: Theta(n)        
height(root)
print(diameter)