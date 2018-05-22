class n:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    if root == None:
        return True
    return check(root.left, root.right)


def check(left,right):
    if left == None and right == None:
        return True
    if left.val != right.val:
        return False
    left_check = check(left.left,right.right)
    right_check = check(left.right,right.left)
    return left_check and right_check

a=n(1)
a.left=n(2)
a.right=n(2)
a.left.left=n(3)
a.right.right=n(3)
a.left.right=n(4)
a.right.left=n(4)
isSymmetric(a)