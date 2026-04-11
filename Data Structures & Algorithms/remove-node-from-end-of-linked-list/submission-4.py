# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = future = head
        if cur.next == None and n== 1:
            return head.next
        while n>0:
            if not future.next:
                return head.next
            future = future.next
            n-=1

        while future.next:
            print(cur.val)
            cur= cur.next
            future = future.next

        cur.next = cur.next.next
        return head