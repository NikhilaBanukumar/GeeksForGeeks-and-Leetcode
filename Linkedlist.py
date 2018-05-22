class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.root=None
        self.size=0

    def insert(self,data):
        node=Node(data)
        if self.root == None:
            self.root =node
            self.size += 1
            return
        root=self.root
        while root.next!=None:
            root=root.next
        root.next=node
        self.size+=1


    def print(self,root):
        while root!=None:
            a=root.data
            print(root.data)
            root=root.next

    def sort_linkedlist(self):
        if self.root==None:
            return
        elif self.size==1:
            return self.root
        ll1=self.root
        ll2=self.root.next
        node1=ll1
        node2=ll2
        i=3
        while i<=self.size:
            if i%2!=0:
                node1.next=node2.next
                node1=node1.next
            else:
                node2.next=node1.next
                node2=node2.next
            i+=1
        node1.next=None
        node2.next=None
        smallest=ll2
        while smallest.next!=None:
            smallest=smallest.next
        if ll1.data<smallest.data:
            root=ll1
        else:
            root=ll2
        while ll2:
            if ll2.data > ll1.data:
                prev = ll1
                ll1 = ll1.next

            else:
                if prev != None:
                    temp = ll2
                    ll2 = ll2.next
                    temp.next = prev.next
                    prev.next = temp
                    ll1 = temp

                else:
                    temp = ll2
                    ll2 = ll2.next
                    temp.next = ll1
                    ll1 = temp
        self.print(root)

ll=Linkedlist()
ll.insert(10)
ll.insert(40)
ll.insert(53)
ll.insert(30)
ll.insert(67)
ll.insert(12)
ll.insert(89)
# print(ll.size)
ll.sort_linkedlist()