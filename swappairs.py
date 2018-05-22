class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def swap_pairs(root):
    cur=root
    while cur and cur.next:
        if cur==root:
            temp=cur.next
            cur.next=temp.next
            temp.next=cur
            root=temp
            prev = cur
            cur=cur.next

        else:
            temp=cur.next
            cur.next=temp.next
            temp.next=cur
            prev.next=temp
            prev=cur
            cur=cur.next
    cur=root
    while root:
        print(root.val)
        root=root.next


root=Node(1)
root.next=Node(2)
root.next.next=Node(3)
root.next.next.next=Node(4)
root.next.next.next.next=Node(5)
swap_pairs(root)
