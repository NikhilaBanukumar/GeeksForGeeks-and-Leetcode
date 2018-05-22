class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        node=Node(data)
        if self.root==None:
            self.root=node
            return node
        current=self.root
        parent=None
        while current:
            parent=current
            if current.data<=data:
                current=current.right
            else:
                current=current.left
        if parent.data<=data:
            parent.right=node
        else:
            parent.left=node
        return self.root

    def print(self,node):
        print(node.data)
        if node.left!=None:
             self.print(node.left)
        if node.right!=None:
            self.print(node.right)

if __name__ =="__main__":
    t=Tree()
    t.insert(10)
    t.insert(5)
    t.insert(12)
    t.insert(2)
    t.insert(8)
    t.insert(11)
    t.insert(14)
    t.print(t.root)


