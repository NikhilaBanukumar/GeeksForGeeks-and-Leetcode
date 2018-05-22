class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None

def height(root):
    if root==None:
        return 0
    else:
        return max(height(root.left),height(root.right))+1

def printlevelorder(root):
    h=height(root)
    print(h)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
printlevelorder(root)