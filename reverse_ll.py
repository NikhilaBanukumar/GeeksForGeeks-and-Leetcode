import copy
class node:
    def __init__(self, x):
        self.val = x
        self.next = None
def reverseList(head):
    root = None
    while head != None:
        if root == None:
            root = copy.copy(head)
            root.next = None
        else:
            temp = copy.copy(head)
            temp.next = root
            root = temp
        head = head.next
    while root!=None:
        print(root.val)
        root=root.next
    return root

head=node(1)
head.next=node(2)
head.next.next=node(3)
head.next.next.next=node(4)
head.next.next.next.next=node(5)
reverseList(head)