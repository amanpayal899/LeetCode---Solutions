# Problem: Binary Tree Inorder Traversal
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Submitted: 2026-07-12_193715 UTC
# URL: https://leetcode.com/submissions/detail/2065401001/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inorder(root):
            if root is None:
                return
            left = inorder(root.left)
            if left is not None:
                result.append(inorder(root.left))
            result.append(root.val)
            right = inorder(root.right)
            if right is not None:
                result.append(inorder(root.right))
            return

        inorder(root)
        return result

