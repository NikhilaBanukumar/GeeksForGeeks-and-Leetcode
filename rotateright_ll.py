class node:
    def __init__(self, x):
        self.val = x
        self.next = None

def rotateRight(head, k):
    n = 0
    root = head
    while root != None:
        n += 1
        root = root.next
    if k>=n:
        k=k%n
    if k==0:
        return head
    else:
        root=head
        while root.next!=None:
            root=root.next
        root.next=head
        j=1
        while j<=n-k:
            if j==n-k:
                root1=head.next
                head.next=None
                break
            else:
                head=head.next
            j+=1
    while root1!=None:
        print(root1.val)
        root1=root1.next


head=node(1)
head.next=node(2)
head.next.next=node(3)
head.next.next.next=node(4)
head.next.next.next.next=node(5)
rotateRight(head,2)