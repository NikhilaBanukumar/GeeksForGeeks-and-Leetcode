class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def iffoundsun(root,sum):
    if root==None:
        return False
    left=iffoundsun(root.left,sum-root.data)
    right=iffoundsun(root.right,sum-root.data)
    if right==False and left==False:
        sum-=root.data
        if sum==0:
            return True
        else:
            return False
    elif right==True or left==True:
        return True


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(8)
root.left.left.right=Node(9)
root.right.left=Node(7)
root.right.right=Node(6)
print(iffoundsun(root,50))