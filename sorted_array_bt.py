class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def convert(a):
    if a==[]:
        return None
    mid=int(len(a)/2)
    root=node(a[mid])
    root.left=convert(a[:mid])
    root.right=convert(a[mid+1:])
    return root

a=[-10,-3,0,5,9]
convert(a)




