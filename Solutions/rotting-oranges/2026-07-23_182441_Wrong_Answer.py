# Problem: Rotting Oranges
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-23_182441 UTC
# URL: https://leetcode.com/submissions/detail/2078764258/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(columns):
                temp = -1
                if grid[r][c] == 2:
                    if r > 0:
                        if grid[r-1][c] == 1:
                            grid[r-1][c] = 2
                            temp = 0

                    if r < rows-1:
                        if grid[r+1][c] == 1:
                            grid[r+1][c] = 2
                            temp = 0

                    if c > 0:
                        if grid[r][c-1] == 1:
                           grid[r][c-1] = 2 
                           temp = 0

                    if c < columns-1:
                        if grid[r][c+1] == 1:
                           grid[r][c+1] = 2
                           temp = 0
                    if temp == 0: 
                        count += 1
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    return -1
        return count 

        

            