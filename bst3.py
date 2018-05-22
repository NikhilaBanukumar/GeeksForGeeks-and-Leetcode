class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class B:
    def __init__(self):
        self.b=0
def without_array(root,k,B):
    if root==None or B.b>=k:
        return
    without_array(root.right,k,B)
    B.b+=1
    if B.b==k:
        print("Largest:"+str(root.data))
        return
    without_array(root.left,k,B)


def inorder(root,array):
    if root==None:
        return
    if root!=None:
        a=root.data
        inorder(root.left, array)
        array.append(root.data)
        inorder(root.right,array)
    return array

root=Node(50)
root.left=Node(30)
root.right=Node(70)
root.left.left=Node(20)
root.left.right=Node(40)
root.right.left=Node(60)
root.right.right=Node(80)
arr=inorder(root,[])
print(arr[len(arr)-3])
a=B()
without_array(root,3,a)
