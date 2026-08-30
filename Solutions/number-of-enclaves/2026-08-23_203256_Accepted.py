# Problem: Number of Enclaves
# Status: Accepted
# Language: python3
# Runtime: 67 ms
# Memory: 22.7 MB
# Submitted: 2026-08-23_203256 UTC
# URL: https://leetcode.com/submissions/detail/2117805720/

from collections import deque
def land_bfs(grid, n, m, total_non_isolated_land, visited, stack):

        while len(stack) != 0:
            r, c = stack.pop()
            for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = r+i, c+j
                if 0<=nr<n and 0<=nc<m:
                    if grid[nr][nc] == 1 and visited[nr][nc] == 0:
                        stack.append((nr, nc))
                        visited[nr][nc] = 1
                        total_non_isolated_land += 1
        return total_non_isolated_land

class Solution:
    

    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [ [0]*m for _ in range(n)]
        ans = 0
        total_land = 0
        total_non_isolated_land = 0
        stack = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    total_land += 1
                    if i==0 or i == (n-1) or j==0 or j==(m-1):
                        visited[i][j] = 1
                        total_non_isolated_land += 1
                        stack.append((i, j))
        if len(stack) == 0:
            return total_land
        
        total_non_isolated_land = land_bfs(grid, n, m, total_non_isolated_land, visited, stack)
        return total_land - total_non_isolated_land


