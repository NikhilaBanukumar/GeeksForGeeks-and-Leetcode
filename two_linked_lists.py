class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        count1=0
        count2=0
        roota = headA
        rootb = headB
        while roota!=None:
            count1+=1
            roota=roota.next
        while rootb!=None:
            count2+=1
            rootb=rootb.next
        roota=headA
        rootb=headB
        diff=count1-count2
        if diff>0:
            while diff!=0:
                roota=roota.next
                diff-=1
        elif diff<0:
            while diff!=0:
                rootb=rootb.next
                diff+=1
        while roota!=rootb:
            roota=roota.next
            rootb=rootb.next
        if roota==rootb and roota!=None:
            return roota
        else:
            return None
headA=ListNode("A")
headA.next=ListNode("B")
headA.next.next=ListNode("C")
headA.next.next.next=ListNode("D")
headB=ListNode("X")
headB.next=ListNode("Y")
headB.next.next=ListNode("Z")
headB.next.next.next=headA.next.next
a=Solution()
b=a.getIntersectionNode(headA,headB)
print(b.val)