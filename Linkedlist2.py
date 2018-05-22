class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self,size):
        self.root=None
        self.size=0
        self.capacity=size

    def insert(self,key,value):
        node=Node(key,value)
        if self.size<self.capacity:
            if self.root==None:
                self.root=node
                self.size+=1
                return
            node.next=self.root
            self.root.prev=node
            self.root=node
            self.size+=1
        else:
            a=self.root.key
            root=self.root
            while root.next!=None:
                root=root.next
            prev=root.prev
            prev.next=None
            node.next = self.root
            self.root = node
        return

    def get(self,key):
        root=self.root
        while root!=None:
            if root==self.root and root.key==key:
                return root.value
            elif root.key==key:
                temp=root
                prev=root.prev
                prev.next=root.next
                temp.next=self.root
                self.root=temp
                return temp.value
            root=root.next

        if root==None:
            return -1

    def print(self):
        root=self.root
        while root!=None:
            print(str(root.key)+":"+str(root.value))
            root=root.next


ll=LinkedList(3)
ll.insert(1,10)
ll.insert(2,20)
ll.insert(3,30)
ll.insert(4,40)
print(ll.get(2))
ll.print()

