class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
prev = None # prev is previous node of root node
def BTToDLL(root): # add root list to prev list and update prev
    global prev

    if root == None:
        return root
        
    head = BTToDLL(root.left)
    
    if prev == None:
        head = root
    else:
        root.left = prev
        prev.right = root
        
    prev = root
    BTToDLL(root.right)
    return head
    
    
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.left = Node(30)
root.right.right = Node(35)

head = BTToDLL(root)
curr = head
tail = None
while(curr):
    print(curr.key, end=' ')
    tail = curr
    curr = curr.right

print()

curr = tail    
while(curr):
    print(curr.key, end=' ')
    curr = curr.left
    