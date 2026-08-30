# Problem: Diameter of Binary Tree
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-13_191410 UTC
# URL: https://leetcode.com/submissions/detail/2066590811/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)
            return 1+max(left, right)

        return (height(root.left) + height(root.right))