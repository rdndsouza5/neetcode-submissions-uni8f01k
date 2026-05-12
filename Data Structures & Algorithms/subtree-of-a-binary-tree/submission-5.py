# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        if not subRoot:
            return True
        
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if self.isSame(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return False
        
    
    def isSame(self, t: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        if not t and not subRoot:
            return True
        if not t and subRoot:
            return False
        if not subRoot and t:
            return False
        if t.val != subRoot.val:
            return False
        
        return self.isSame(t.left, subRoot.left) and self.isSame(t.right, subRoot.right)
        
