# Problem: Count Complete Tree Nodes
# Status: Accepted
# Language: python3
# Runtime: 4 ms
# Memory: 23.7 MB
# Submitted: 2026-07-21_204653 UTC
# URL: https://leetcode.com/submissions/detail/2076369086/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            return 1+dfs(node.left)+dfs(node.right)

        return dfs(root)