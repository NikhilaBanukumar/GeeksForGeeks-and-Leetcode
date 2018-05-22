class newNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def remove_nodes(root,sum,b,parent):
    if root==None:
        return None
    b+=root.data
    if parent==None:
        parent=root
    m = root.data
    n = parent.data
    if b>=sum:
        return
    else:
        if root.left==None and root.right==None:
            if parent.left and parent.left.data==root.data:
                parent.left=None
            else:
                parent.right=None
            return
        else:
            parent=root
            remove_nodes(root.left,sum,b,parent)
            remove_nodes(root.right,sum,b,parent)
            if root.left==None and root.right==None:
                if parent.left and parent.left.data==root.data:
                    parent.left=None
                else:
                    parent.right=None
            return


def printbt(root):
    if root!=None:
        print(root.data)
        printbt(root.left)
        printbt(root.right)
    return


root = newNode(1);
root.left = newNode(2);
root.right = newNode(3);
root.left.left = newNode(4);
root.left.right = newNode(5);
root.right.left = newNode(6);
root.right.right = newNode(7);
root.left.left.left = newNode(8);
root.left.left.right = newNode(9);
root.left.right.left = newNode(12);
root.right.right.left = newNode(10);
root.right.right.left.right = newNode(11);
root.left.left.right.left = newNode(13);
root.left.left.right.right = newNode(14);
root.left.left.right.right.left = newNode(15);
remove_nodes(root,45,0,None)
printbt(root)
