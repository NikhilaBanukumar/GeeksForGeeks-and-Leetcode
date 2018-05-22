class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def calculate_sum(a,b,sum):
    if a==None :
        return False
    if a.data+b==sum and a.left==None and a.right==None:
        return True
    else:
        b+=a.data
        return calculate_sum(a.left,b,sum) or calculate_sum(a.right,b,sum)

sum= 10
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)
print(calculate_sum(root,0,sum))