# Problem: Search a 2D Matrix II
# Status: Accepted
# Language: python3
# Runtime: 141 ms
# Memory: 25.5 MB
# Submitted: 2026-08-19_182438 UTC
# URL: https://leetcode.com/submissions/detail/2113113799/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r = len(matrix)
        c = len(matrix[0])
        i = 0
        j = c-1
        while i>=0 and i<r and j>=0 and j<c:

            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                i+=1
            else:
                j-=1

        return False

                