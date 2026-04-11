# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        while head:

            nodes.append(head)
            head = head.next
        
        if n==len(nodes):
            return nodes[0].next
        
        nodes[len(nodes)-n-1].next = nodes[len(nodes)-n-1].next.next

        return nodes[0]