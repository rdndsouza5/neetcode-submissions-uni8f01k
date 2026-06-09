# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        pos= 0
        def dfs(l, r):
            nonlocal pos
            if pos>= len(preorder) or l>r:
                return
            node = TreeNode(preorder[pos])
            pos+=1
            index = indices[node.val]
            node.left = dfs(l, index-1)
            node.right = dfs(index+1, r)
            return node
        return dfs(0, len(inorder)-1)