# burn a binary tree from a leaf
# => farthest node from the given leaf

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        
class Distance: # value as object
    def __init__(self, d):
        self.val = d
        
# return height
# set dist if given leaf is a descendant        
res = 0
def burnTime(root, leaf, dist):
    global res
    
    if root == None:
        return 0

    if root.key == leaf:
    	dist.val = 0
    	return 1

    ldist = Distance(-1)
    rdist = Distance(-1)

    lh = burnTime(root.left, leaf, ldist)
    rh = burnTime(root.right, leaf, rdist)

    if ldist.val != -1: # if root is ancestor of leaf
        # get dist from leaf to root
   		dist.val = ldist.val + 1
        # height of subtree on the other side + dist
        # check if burnning to the other subtree would take longer
   		res = max(res, rh + dist.val)
    elif rdist.val != -1:
   	    dist.val = rdist.val + 1
   	    res = max(res, dist.val + lh)
        
    return max(lh, rh) + 1


root = Node(10)    
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.left.left = Node(60)
root.left.left.left.left = Node(70)

burnTime(root, 50, Distance(-1))

print(res)
