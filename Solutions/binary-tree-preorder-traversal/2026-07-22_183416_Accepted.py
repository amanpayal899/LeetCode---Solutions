# Problem: Binary Tree Preorder Traversal
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.5 MB
# Submitted: 2026-07-22_183416 UTC
# URL: https://leetcode.com/submissions/detail/2077560571/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node, result):
            if node is None:
                return
            result.append(node.val)
            preorder(node.left, result)
            preorder(node.right, result)
            return
        result = []
        preorder(root, result)
        return result