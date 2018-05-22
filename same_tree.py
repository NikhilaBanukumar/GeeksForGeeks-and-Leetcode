class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def isSameTree(p, q):
    if p == None and q == None:
        return True
    if p.val != q.val:
        return False
    else:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

a=node(1)
a.left=node(2)
a.right=node(3)
b=node(1)
b.left=node(2)
b.right=node(3)
print(isSameTree(a,b))