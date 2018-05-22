class node:
    def __init__(self,x):
        self.val=x
        self.next=None

def ll(head):
    root=head
    prev=None
    while root!=None:
        if root.val==2:
            prev.next=root.next
            break
        else:
            prev=root
            root=root.next
    while head!=None:
        print(head.val)
        head=head.next
head=node(1)
head.next=node(2)
head.next.next=node(3)
ll(head)