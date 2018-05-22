class node:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElements(head, val):
    if head == None:
        return head
    if head.next == None:
        if head.val == val:
            return None
        else:
            return head
    root = head
    prev = None
    while root != None:
        if root.val == val:
            if root == head:
                head = head.next
                root = head
            else:
                prev.next = root.next
                root = prev.next
        else:
            prev = root
            root = root.next

    while head!=None:
        print(head.val)
        head=head.next

head=node(1)
head.next=node(1)
# head.next.next=node(6)
# head.next.next.next=node(3)
# head.next.next.next.next=node(4)
# head.next.next.next.next.next=node(5)
# head.next.next.next.next.next.next=node(6)
removeElements(head,1)