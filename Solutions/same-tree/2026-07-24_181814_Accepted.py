# Problem: Same Tree
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Submitted: 2026-07-24_181814 UTC
# URL: https://leetcode.com/submissions/detail/2079957772/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def dfs(node,arr):
            if node is None:
                return 0
            left = dfs(node.left,arr)
            arr.append(left)
            arr.append(node.val)
            right = dfs(node.right,arr)
            arr.append(right)
            
        dfs(p,arr1)
        dfs(q, arr2)
        if len(arr1) != len(arr2):
            return False
        l = len(arr1)
        for i in range(l):
            if arr1[i] != arr2[i]:
                return False

        return True