# Problem: Balanced Binary Tree
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-15_153513 UTC
# URL: https://leetcode.com/submissions/detail/2068793423/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 | right == -1:
                return -1
            if abs(left-right)>1:
                return -1
            else:
                return 1+max(left, right)

        result = dfs(root)
        if result == -1:
            return False
        return True

            

