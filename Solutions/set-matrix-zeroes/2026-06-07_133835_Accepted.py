# Problem: Set Matrix Zeroes
# Status: Accepted
# Language: python3
# Runtime: 3570 ms
# Memory: 20.2 MB
# Submitted: 2026-06-07_133835 UTC
# URL: https://leetcode.com/submissions/detail/2025399978/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_track = []
        col_track = []
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_track.append(i)
                    col_track.append(j)
        for i in range(r):
            for j in range(c):
                if i in row_track or j in col_track:
                    matrix[i][j] = 0