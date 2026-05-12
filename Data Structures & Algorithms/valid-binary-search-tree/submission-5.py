# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.max_int= float("-inf")
        return self.inorder(root)


    def inorder(self,node)-> bool:
        if not node:
            return True
 
        if not self.inorder(node.left):
            return False
        if node.val<= self.max_int:
            return False
        self.max_int = max(self.max_int, node.val)
        return self.inorder(node.right)

        

