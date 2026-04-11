# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = right = head
        while right:
            right = right.next
            count+=1
        
        removeIndex = count - n

        if removeIndex == 0:
            return head.next

        for i in range(count-1):
            if (i+1) == removeIndex:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head