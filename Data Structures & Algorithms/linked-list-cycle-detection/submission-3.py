# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        cur = head
        future = cur.next
        while cur and future:
            if cur == future:
                return True
            if cur.next:
                cur = cur.next
            else:
                break
            if future.next and future.next.next:
                future = future.next.next
            else:
                break
        return False

        
            