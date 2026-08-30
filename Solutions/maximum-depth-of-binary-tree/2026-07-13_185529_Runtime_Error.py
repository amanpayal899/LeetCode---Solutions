# Problem: Maximum Depth of Binary Tree
# Status: Runtime Error
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-13_185529 UTC
# URL: https://leetcode.com/submissions/detail/2066574672/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([])
        height = 0
        queue.append(root)
        while queue:
            height += 1
            level_size = len(queue)
            for _ in range(level_size):
                e = queue.popleft()
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
        return height