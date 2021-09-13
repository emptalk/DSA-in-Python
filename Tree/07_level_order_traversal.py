from collections import deque

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

# time complixity: theta(n)
# auxiliary space: O(n), theta(w)
def printLevel(root):
    if root == None:
        return
    
    q = deque()
    q.append(root)
    while q:
        curr = q.popleft()
        print(curr.key, end=' ')
        
        if curr.left != None:
            q.append(curr.left)
        if curr.right != None:
            q.append(curr.right)
        

root = Node(10)
root.left = Node(15)
root.right = Node(20)
root.left.left = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
root.right.left.left = Node(60)
root.right.left.right = Node(70)

printLevel(root)
