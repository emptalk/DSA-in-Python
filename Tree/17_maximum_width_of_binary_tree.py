import queue

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
def maxWidth(root):
    if root == None:
        return 0
    
    q = queue.Queue()
    q.put(root)
    res = 0
    
    while q.empty() == False:
        count = q.qsize()
        res = max(res, count)
        
        for i in range(count):
            curr = q.get()
            if curr.left != None:
                q.put(curr.left)
            if curr.right != None:
                q.put(curr.right)
    
    return res
                
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)

print(maxWidth(root))