# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int: 
        queue = deque([(root, float("-inf"))])
        count = 0
        while queue:
            node, val = queue.popleft()
            if node:
                if val > node.val:
                    queue.append((node.left, val))
                    queue.append((node.right, val))
                else:
                    count+=1
                    queue.append((node.left, node.val))
                    queue.append((node.right, node.val))

        return count
                    

                
        