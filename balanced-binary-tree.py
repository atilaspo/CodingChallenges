# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        self.balanced = True

        def dfs(curr):
            if curr is None:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            if abs(left - right) > 1:
                self.balanced = False
            return 1 + max(left, right)
        
        dfs(root)
        return self.balanced