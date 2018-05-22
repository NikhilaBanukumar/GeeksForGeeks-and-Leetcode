class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

class Tree:
    def insert(self,root,key):
        if not root:
            return Node(key)
        elif root.data<key:
            root.insert(root.right,key)
        else:
            root.insert(root.left,key)
        root.height=1+max(self.getheight(root.left),self.getheight(root.right))
        balance=self.getbalance(root)
        if balance>1 and key<root.left.data:
            return self.rightrotate(root)
        if balance<-1 and 

