# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.min_int= float("+inf")
        return self.inorder(root)


    def inorder(self,node)-> bool:
        if not node:
            return True
 
        if not self.inorder(node.right):
            return False
        if node.val>= self.min_int:
            return False
        self.min_int = min(self.min_int, node.val)
        return self.inorder(node.left)

        

