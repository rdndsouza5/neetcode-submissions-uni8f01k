# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        return self.loop(head.next, head.next.next)
        
    def loop(self, slow, fast) -> bool:
        if not fast or not fast.next:
            return False
        if slow == fast:
            return True
        return self.loop(slow.next, fast.next.next)