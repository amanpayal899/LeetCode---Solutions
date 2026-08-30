# Problem: Diameter of Binary Tree
# Status: Accepted
# Language: python3
# Runtime: 4 ms
# Memory: 22.3 MB
# Submitted: 2026-07-14_170303 UTC
# URL: https://leetcode.com/submissions/detail/2067655735/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0, 0
            leftd = dfs(root.left)
            rightd = dfs(root.right)
            diameter = max(leftd[0], rightd[0])
            if diameter < leftd[1]+rightd[1]:
                diameter = leftd[1]+rightd[1]

            return diameter,1 + max(leftd[1], rightd[1])
        l = dfs(root)
        return l[0]