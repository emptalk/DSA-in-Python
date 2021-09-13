import queue

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


def printLeft(root):
    if root == None:
        return
    
    q = queue.Queue()
    q.put(root)
    
    while q.empty() == False:
        count = q.qsize()
        
        for i in range(count): # i: 0 ~ count-1
            curr = q.get()
            
            # print only first node in queue
            if i == 0:
                print(curr.key, end=' ')
                
            if curr.left != None:
                q.put(curr.left)
            if curr.right != None:
                q.put(curr.right)
    
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)    

printLeft(root)