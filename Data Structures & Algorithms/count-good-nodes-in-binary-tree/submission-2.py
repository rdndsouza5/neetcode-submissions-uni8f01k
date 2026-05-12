# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int: 
        if not root:
            return 0
        
        count = 0
        
        def dfs(node, maxVal)-> int:
            count =0
            if not node:
                return 0
            if node.val >=maxVal:
                count+=1
                maxVal = node.val
            return count+ dfs(node.left, maxVal)+dfs(node.right, maxVal)
            

        
        return dfs(root, float("-inf"))

            
        