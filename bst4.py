class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

curr=tree(0)
def k_largest(root,k):
    if root==None:
        return k
    if root!=None:
        curr.data=root.data
        k=k_largest(root.right,k)
        if k==0:
            return k
    k-=1
    if k==0:
        curr.data=root.data
        return k
    else:
        if root.left!=None:
            k=k_largest(root.left,k)
            return k
        else:
            return k


a=tree(20)
a.left=tree(8)
a.left.left=tree(4)
a.left.right=tree(12)
a.right=tree(25)
a.right.left=tree(23)
a.right.left.left=tree(22)
a.right.right=tree(30)
k_largest(a,6)
print(curr.data)