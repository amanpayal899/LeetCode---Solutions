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
