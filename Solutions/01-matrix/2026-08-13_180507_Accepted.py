# Problem: 01 Matrix
# Status: Accepted
# Language: python3
# Runtime: 155 ms
# Memory: 23.5 MB
# Submitted: 2026-08-13_180507 UTC
# URL: https://leetcode.com/submissions/detail/2105813733/

from collections import deque

class Solution:
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        result = copy.deepcopy(mat)
        visited = [ [0]*cols for _ in range(rows)]

        def dfs(rows, cols, queue, result, visited):
            for  r in range(rows):
                for c in range(cols):
                    if result[r][c] == 0:
                        queue.append( (r, c, 0))
                        visited[r][c] = 1

            while len(queue)!=0:
                r, c, dis = queue.popleft()
                result[r][c] = dis
                for i, j in [ [-1,0], [0, 1], [1,0], [0, -1] ]:
                    nr, nc = r+i, c+j
                    if nr<0 or nr>=rows or nc<0 or nc>=cols or visited[nr][nc] :
                        continue
                    queue.append( (nr, nc, dis+1) )
                    visited[nr][nc]=1


        dfs(rows, cols, queue, result, visited)
        return result
        