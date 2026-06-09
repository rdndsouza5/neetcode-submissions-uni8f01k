# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {key:idx for idx, key in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(l, r):
            if l>r:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx +=1
            root = TreeNode(root_val)
            pos = indices[root_val]
            root.left = dfs(l, pos-1)

            root.right = dfs(pos+1, r)

            return root
        return dfs(0, len(preorder)-1)

         