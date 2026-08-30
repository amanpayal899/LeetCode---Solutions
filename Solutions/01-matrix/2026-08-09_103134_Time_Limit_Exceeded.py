# Problem: 01 Matrix
# Status: Time Limit Exceeded
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-09_103134 UTC
# URL: https://leetcode.com/submissions/detail/2100220192/

from collections import deque
class Solution:
    def nearestZero(self, cpy, visited, i, j, rows, col):
        
        queue = deque()
        queue.append((i, j, 0))
        while queue:
            i, j, dis = queue.popleft()
            for r, c in [[-1,0], [0, 1], [1, 0], [0, -1]]:
                nr, nc = i+r, j+c
                if nr>=rows or nr<0 or nc>=col or nc<0:
                    continue
                if cpy[nr][nc] == 0:
                    return dis+1
                if  visited[nr][nc] == False:
                    queue.append((nr, nc, dis+1))
                    visited[nr][nc] = True

                
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        cpy = copy.deepcopy(mat)
        
        rows = len(mat)
        col = len(mat[0])
        
        for i in range(rows):
            for j in range(col):
                if cpy[i][j] == 0:
                    continue
                visited = [ [False]*col  for _ in range(rows)]
                cpy[i][j] = self.nearestZero(cpy, visited, i, j, rows, col)
        return cpy