# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        rootStr = self.generateString(root)
        subRootStr = self.generateString(subRoot)
        print(rootStr)
        print(subRootStr)
        if rootStr.find(subRootStr) == -1:
            return False
        return True

    def generateString(self, p)-> str:
        string = ""
        if not p:
            return "."
        else: 
            string += str(p.val)
       
        return string + self.generateString(p.left) + self.generateString(p.right)