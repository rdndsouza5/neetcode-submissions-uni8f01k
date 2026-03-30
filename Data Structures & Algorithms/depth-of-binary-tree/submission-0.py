# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root,0)
        

    def depth(self, root, count)->int:
        if not root:
            return count
        count+=1
        countLeft = self.depth(root.left,count)
        countRight= self.depth(root.right,count)
        count = max(countLeft, countRight)
        return count