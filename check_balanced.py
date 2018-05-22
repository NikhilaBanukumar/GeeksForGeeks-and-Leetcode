class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def height(root):
    if root==None:
        return 0
    left=height(root.left)
    right=height(root.right)
    return 1+left if left>right else 1+right

map={}
def check(root):

    if root==None:
        return True
    left=check(root.left)
    right=check(root.right)
    if left==True and right==True:
        if root.left in map:
            left_height=map[root.left]
        else:
            left_height=height(root.left)
        if root.right in map:
            right_height=map[root.right]
        else:
            right_height=height(root.right)
        if root not in map:
            map[root]=left_height+1 if left_height>right_height else right_height+1
        if abs(left_height - right_height) > 1:
            return False
        else:
            return True
    else:
        return False

root=Node(1)
root.left=Node(2)
root.right=Node(2)
root.left.left=Node(3)
root.left.right=Node(3)
root.left.left.left=Node(4)
root.left.left.right=Node(4)
print(check(root))