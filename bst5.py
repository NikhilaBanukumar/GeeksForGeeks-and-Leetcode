class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def getnodecount(root,min,max):
    if root==None:
        return 0
    if root.data>=min and root.data<=max:
        return 1+getnodecount(root.left,min,max)+getnodecount(root.right,min,max)
    if root.data>max:
        return getnodecount(root.left,min,max)
    if root.data<min:
        return getnodecount(root.right,min,max)

root=Tree(10)
root.left=Tree(6)
root.left.left=Tree(4)
root.left.left.right=Tree(5)
root.left.right=Tree(7)
root.right=Tree(50)
root.right.left=Tree(40)
root.right.right=Tree(67)
print(getnodecount(root,5,45))