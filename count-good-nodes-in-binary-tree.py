# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        queue = deque([(root, root.val)])

        while queue:
            node, current_max = queue.popleft()

            if node.val >= current_max:
                count += 1
            
            new_max = max(node.val, current_max)

            if node.right is not None:
                queue.append((node.right, new_max))
            if node.left is not None:
                queue.append((node.left, new_max))
        
        return count