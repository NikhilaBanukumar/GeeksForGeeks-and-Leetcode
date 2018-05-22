class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Flag:
    flag=0

def distance_between_nodes(root, node1, node2,Flag):
    if root==None:
        return 0
    a=root.data
    if root==node1 or root==node2:
        left = distance_between_nodes(root.left, node1, node2,Flag)
        right = distance_between_nodes(root.right, node1, node2,Flag)
        if left+right>0:
            Flag.flag+=2
            return left+right
        return 1+left+right
    left=distance_between_nodes(root.left,node1,node2,Flag)
    right=distance_between_nodes(root.right,node1,node2,Flag)
    if left!=0 and right!=0:
        Flag.flag+=2
        return left+right
    elif right!=0 or left!=0:
        if Flag.flag==2:
            return left+right
        Flag.flag += 1
        return 1+left+right
    else:
        return 0


root = newNode(1);
root.left = newNode(2);
root.right = newNode(3);
root.left.left = newNode(4);
root.left.right = newNode(5);
root.right.left = newNode(6);
root.right.right = newNode(7);
print(distance_between_nodes(root,root.left.left,root.left.right,Flag))