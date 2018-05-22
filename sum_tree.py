class node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def hasPathSum(root, sum):
    if root == None:
        return False
    if root.left==None and root.right==None:
        if sum-root.val==0:
            return True
        return False
    left = hasPathSum(root.left, sum - root.val)
    right = hasPathSum(root.right, sum - root.val)

    return left or right

root=node(5)
root.left=node(4)
root.right=node(8)
root.left.left=node(11)
root.right.left=node(13)
root.right.right=node(4)
root.left.left.left=node(7)
root.left.left.right=node(2)
root.right.right.left=node(1)
print(hasPathSum(root,22))