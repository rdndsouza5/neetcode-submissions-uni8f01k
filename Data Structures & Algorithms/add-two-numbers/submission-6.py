# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode= ListNode(0)
        cur = dummyNode
        curVal = 0    
        while l1 or l2:
            if l1:
                curVal += l1.val
                l1 = l1.next
            if l2:
                curVal += l2.val
                l2 = l2.next
            cur.next = ListNode(curVal%10)
            cur= cur.next
            curVal = curVal //10
        if curVal:
            cur.next = ListNode(curVal)
        return dummyNode.next