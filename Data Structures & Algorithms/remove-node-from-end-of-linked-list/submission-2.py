# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        future = head
        if cur.next == None and n== 1:
            return head.next
        while n>0:
            future = future.next
            n-=1

        while future:
            cur= cur.next
            future = future.next

        cur.next = cur.next.next
        return dummy.next
