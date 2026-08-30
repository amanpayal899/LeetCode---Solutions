# Problem: Diameter of Binary Tree
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-14_164257 UTC
# URL: https://leetcode.com/submissions/detail/2067627967/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root, diameter):
            if root is None:
                return [0, 0]
            leftd = dfs(root.left, diameter)
            rightd = dfs(root.right, diameter)
            if diameter < leftd[1]+rightd[1]:
                diameter = leftd[1]+rightd[1]

            return [diameter,1 + max(leftd[1], rightd[1])]
        l = dfs(root, 0)
        return l[0]