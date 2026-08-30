# Problem: Binary Tree Postorder Traversal
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Submitted: 2026-08-26_212834 UTC
# URL: https://leetcode.com/submissions/detail/2121300449/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       
        def dfs( node, result ):
            if node == None:
                return
            dfs( node.left, result )
            dfs( node.right, result )
            result.append( node.val )
        
        result = []
        dfs(root, result)
        return result
