class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
main=[]
def build(q):
    if q==[]:
        return main
    a=[]
    qu=[]
    for i in q:
        a.append(i.val)
        if i.left!=None:
            qu.append(i.left)
        if i.right!=None:
            qu.append(i.right)
    main.append(a)
    return build(qu)

def level_order(a):


a=node(3)
a.left=node(9)
a.right=node(20)
a.left.left=node(5)
a.left.right=node(6)
a.right.left=node(7)
a.right.right=node(8)
print(level_order(a))
