class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class Index:
    def __init__(self):
        self.i=0
def subsequence_in_bt(root,array,a):
    if root==None:
        if a.i==0:
            return False
        else:
            return True

    if a.i==len(array):
        return True
    b=root.data
    n=a
    if root.data==array[a.i]:
        a.i+= 1
        if root.left!=None:
            return subsequence_in_bt(root.left,array,a) and subsequence_in_bt(root.right,array,a)
        elif root.right!=None:
            return subsequence_in_bt(root.right,array,a)
        else:
            return subsequence_in_bt(root.left,array,a)
    else:
        if root.data not in array:
            if root.left!=None:
                return subsequence_in_bt(root.left,array,a) or subsequence_in_bt(root.right,array,n)
            elif root.right != None:
                return subsequence_in_bt(root.right, array, a)
            else:
                return subsequence_in_bt(root.left, array, a)
        else:
            return False

root=Node(5)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(1)
root.left.right=Node(4)
root.left.right.left=Node(6)
root.left.right.right=Node(8)
a=Index()
print(subsequence_in_bt(root,[2,1,3],a))