from collections import deque

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def printSpiral(root):
    if root == None:
        return
        
    s1 = deque()
    s2 = deque()
    
    s1.append(root)
    while q:
        count = len(q)
        for i in range(count):
            curr = q.popleft()
            
            if reverse:
                s.append(curr.key)
            else:
                print(curr.key, end=' ')
                
            # queue next level
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
                
        if reverse:
            while s:
                print(s.pop(), end=' ')
                
        reverse = not reverse
        print() # optional 
          
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

printSpiral(root)
