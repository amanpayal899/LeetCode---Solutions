# Problem: Rotate Image
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19 MB
# Submitted: 2026-06-07_185627 UTC
# URL: https://leetcode.com/submissions/detail/2025666957/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            j = 0
            while j<i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1

        
        for i in range(n):
            p1 = 0
            p2 = n-1
            while p1<p2:
                matrix[i][p1], matrix[i][p2] = matrix[i][p2], matrix[i][p1]
                p1 += 1
                p2 -= 1
            