# Problem: Maximum Depth of Binary Tree
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 22.8 MB
# Submitted: 2026-07-11_202928 UTC
# URL: https://leetcode.com/submissions/detail/2064282372/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def preorder(node):
            if node is None:
                return 0
            return 1 + max(preorder(node.left), preorder(node.right))
        return preorder(root)