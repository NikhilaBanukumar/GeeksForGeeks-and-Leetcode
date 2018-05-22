class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if head==None:
        return False
    i = head
    j=None
    if i.next!= None:
        j = i.next.next
    while j != None:
        if i == j:
            return True
        else:
            i = i.next
            if j.next==None:
                return False
            j = j.next.next
    return False
head=None
print(hasCycle(head))
