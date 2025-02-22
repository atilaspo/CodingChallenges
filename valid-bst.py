# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True

        def dfs(root):
            nonlocal valid
            if root is None:
                return
            
            if root.left is not None and root.left.val >= root.val:
                valid =  False

            if root.right is not None and root.right.val <= root.val:
                valid =  False

            dfs(root.right)
            dfs(root.left)

        dfs(root)
        return valid