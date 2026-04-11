# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mul = 1 
        res = 0
        while l1 or l2:
            a, b = 0, 0
            if l1:
                a= l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            res = res + (a +b)*mul
            mul = mul* 10
           
        prev = None
        head = cur = ListNode(0)
        while res >0:
            tmp = res % 10
            cur.val = tmp
            if prev:
                prev.next = cur
            prev = cur
            res = res//10
            cur = ListNode(0)
        return head

            