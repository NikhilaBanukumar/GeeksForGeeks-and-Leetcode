class newNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
list=[]
def find_both_nodes(root,node1,node2):
    if root==None:
        return False
    a=root.data
    if root==node1 or root==node2:
        rootleft = find_both_nodes(root.left, node1, node2)
        rootright = find_both_nodes(root.right, node1, node2)
        if rootleft or rootright:
            list.append(root.data)
        return True

    rootleft=find_both_nodes(root.left,node1,node2)
    rootright=find_both_nodes(root.right,node1,node2)
    if rootleft and rootright:
        list.append(root.data)
        return True
    elif rootleft or rootright:
        if list!=[]:
            list.append(root.data)
        return True
    else:
        return False

root = newNode(1);
root.left = newNode(2);
root.right = newNode(3);
root.left.left = newNode(4);
root.left.right = newNode(5);
root.right.left = newNode(6);
root.right.right = newNode(7);
root.left.left.left = newNode(8);
root.right.left.left = newNode(9);
root.right.left.right = newNode(10);
find_both_nodes(root,root.left.left,root)
print(list)