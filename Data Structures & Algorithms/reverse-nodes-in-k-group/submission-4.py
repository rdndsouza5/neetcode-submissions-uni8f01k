# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        prevGroup = dummyNode

        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                break
            groupNext = kth.next
            prev, curr= kth.next, prevGroup.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr 
                curr = tmp
            tmp = prevGroup.next 
            prevGroup.next = kth
            prevGroup = tmp

        
        return dummyNode.next
    
    def getKth(self, curr, n):
        while curr and n>0:
            n-=1
            curr = curr.next
        return curr