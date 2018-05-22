class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
i=0
def construct(inorder,preorder):
    global i
    if i==len(preorder):
        return
    if len(inorder)==1:
        root=Node(inorder[0])
        return root
    for j in range(len(inorder)):
        if inorder[j]==preorder[i]:
            root=Node(inorder[j])
            break
    if j!=0:
        i+=1
        root.left=construct(inorder[:j],preorder)
    if j!=len(inorder)-1:
        a=i
        i+=1
        root.right=construct(inorder[j+1:],preorder)
    return root

def printit(root):
    if root!=None:
        printit(root.left)
        print(root.data)
        printit(root.right)

inorder=['D','B','E','A','F','C']
preorder=['A','B','D','E','C','F']
root=construct(inorder,preorder)
printit(root)