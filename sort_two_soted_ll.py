class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
def mergeTwoLists(l1, l2):
    root = None
    if l2.val<l1.val:
        temp=l1
        l1=l2
        l2=temp
    while l1 and l2:
        if root == None:
            root = l1
        if l1.val<l2.val:
            temp=l2
            l2=l2.next
            temp.next=l1.next
            l1.next=temp
            l1=temp.next

    while root:
        print(root.val)
        root=root.next

l1=ListNode(1)
l1.next=ListNode(4)
l1.next.next=ListNode(6)
l2=ListNode(3)
l2.next=ListNode(5)
l2.next.next=ListNode(8)
mergeTwoLists(l1,l2)