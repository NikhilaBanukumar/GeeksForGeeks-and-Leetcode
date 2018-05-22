class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
class doublyLinked:
    def __init__(self,size):
        self.root=None
        self.tail=None
        self.size=0
        self.capacity=size

    def get(self,node):
        if node==self.root:
            return
        prev=node.prev
        prev.next=node.next
        if node.next!=None:
            node.next.prev=prev
        node.next=self.root
        self.root.prev=node
        self.root=node

    def insert(self,node):
        if self.root==None:
            self.root=node
            self.tail=node
            self.size+=1
        elif self.size<self.capacity:
            self.size+=1
            node.next=self.root
            self.root.prev=node
            self.root=node
        else:
            remove=self.tail.key
            prev=self.tail.prev
            prev.next=self.tail.next
            self.tail=prev
            node.next=self.root
            self.root.prev=node
            self.root=node
            return remove

    def print(self):
        root=self.root
        while root!=None:
            print(root.key)
            root=root.next

class LRU_cacche:
    def __init__(self,size):
        self.dll=doublyLinked(size)
        self.dict={}
        self.capacity=size

    def insert(self,key,value):
        if key not in self.dict:
            node = Node(key, value)
            if len(self.dict)<self.capacity:
                self.dict[key]=node
                self.dll.insert(node)
            else:
                keyremoved=self.dll.insert(node)
                self.dict.pop(keyremoved)
                self.dict[key]=node
        else:
            self.dict[key].value=value
            self.dll.get(self.dict[key])

    def print(self):
        self.dll.print()

    def get(self,key):
        if key not in self.dict:
            return -1
        else:
            self.dll.get(self.dict[key])
            return self.dict[key].value

a=LRU_cacche(3)
a.insert(1,10)
a.insert(2,20)
a.insert(3,30)
a.insert(4,40)
a.insert(4,50)
a.get(2)
a.get(4)
a.get(3)
a.print()