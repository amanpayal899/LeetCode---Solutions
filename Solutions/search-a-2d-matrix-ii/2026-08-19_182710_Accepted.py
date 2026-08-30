# Problem: Search a 2D Matrix II
# Status: Accepted
# Language: python3
# Runtime: 152 ms
# Memory: 25.6 MB
# Submitted: 2026-08-19_182710 UTC
# URL: https://leetcode.com/submissions/detail/2113117356/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r = len(matrix)
        c = len(matrix[0])
        i = 0
        j = c-1
        while i<r and j>=0:

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i+=1
            else:
                j-=1

        return False

                