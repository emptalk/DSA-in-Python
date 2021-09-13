class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

maxLevel = 0  # max printed level
def printLeft(root, level):
    global maxLevel

    if root == None:
        return
    
    if maxLevel < level:
        print(root.key, end=' ')
        maxLevel = level
    
    printLeft(root.left, level + 1)
    printLeft(root.right, level + 1)

def printLeftView(root):
    global maxLevel
    maxLevel = 0
    
    printLeft(root, 1)
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)    

printLeftView(root)