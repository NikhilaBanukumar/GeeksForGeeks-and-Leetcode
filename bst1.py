class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def find_lca(a,node1,node2):
    b=a.data
    c=node1.data
    d=node2.data
    if a==None:
        return None
    if a.data==node1.data:
        return node1
    if a.data==node2.data:
        return node2
    if a.data>node1.data and a.data>node2.data:
        return find_lca(a.left,node1,node2)
    elif a.data<node1.data and a.data<node2.data:
        return find_lca(a.right,node1,node2)
    else:
        return a


def iterative(a,node1,node2):
    while a!=None:
        if a.data==node1.data:
            return node1
        if a.data==node2.data:
            return node2
        if a.data>node1.data and a.data>node2.data:
            a=a.left
        elif a.data<node1.data and a.data<node2.data:
            a=a.right
        else:
            return a


a=Node(20)
a.right=Node(22)
a.left=Node(8)
a.left.left=Node(4)
a.left.right=Node(12)
a.left.right.left=Node(10)
a.left.right.right=Node(14)
b=find_lca(a,a.left,a.left.right.right)
c=iterative(a,a.left,a.left.right.right)
print(b.data)
print(c.data)