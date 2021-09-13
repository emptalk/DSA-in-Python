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

print('height')
print(height(root))