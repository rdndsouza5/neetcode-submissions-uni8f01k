# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)== 0:
            return None
        res= ListNode(0)
        cur = res
        minHeap = []

        for lst in lists:
            if  lst:
                heapq.heappush(minHeap,NodeWrapper(lst))
        while minHeap:
            nodeWrapper = heapq.heappop(minHeap)
            cur.next = nodeWrapper.node
            cur = cur.next
            if nodeWrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(nodeWrapper.node.next))
        
        return res.next
