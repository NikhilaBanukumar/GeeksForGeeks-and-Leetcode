class Listnode:
    def __init__(self,val):
        self.val=val
        self.next=None

def remove_node(root,n):
    if root==None:
        return None
    pointer=root
    count=0
    while pointer:
        count+=1
        pointer=pointer.next
    pointer=root
    rootnew=None
    n=(count-n)+1
    count=0
    while pointer:
        count+=1
        if count==n:
            if pointer==root:
                root=pointer.next
                break
            else:
                prev.next=pointer.next
                break
        else:
            prev=pointer
            pointer=pointer.next

    return root




root=Listnode(1)
root.next=Listnode(2)
root.next.next=Listnode(3)
root.next.next.next=Listnode(4)
root.next.next.next.next=Listnode(5)
remove_node(root,2)