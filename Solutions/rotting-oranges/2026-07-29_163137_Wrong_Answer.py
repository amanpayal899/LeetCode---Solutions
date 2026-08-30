# Problem: Rotting Oranges
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-29_163137 UTC
# URL: https://leetcode.com/submissions/detail/2086405760/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        gridCopy = copy.deepcopy(grid)
        rows = len(grid)
        columns = len(grid[0])
        mins = 0
        freshCount =0
        queue = deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshCount += 1

        while len(queue) != 0:
            size = len(queue)
            while size:
                i, j = queue.popleft()
                
                if i!=0 and gridCopy[i-1][j]==1:
                    gridCopy[i-1][j] = 2
                    freshCount -= 1
                    queue.append((i-1, j))
                if i != rows-1 and gridCopy[i+1][j]==1:
                    gridCopy[i+1][j] = 2
                    freshCount -= 1
                    queue.append( (i+1, j))
                if j!=0 and gridCopy[i][j-1]==1:
                    gridCopy[i][j-1] = 2
                    queue.append((i, j-1))
                    freshCount -= 1
                if j!= columns-1 and gridCopy[i][j+1] == 1:
                    gridCopy[i][j+1] = 2
                    queue.append((i, j+1))
                    freshCount -= 1
                size -= 1
            mins += 1
        if freshCount == 0:
            return mins-1
        return -1