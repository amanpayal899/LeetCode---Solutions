# Problem: Flood Fill
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.8 MB
# Submitted: 2026-08-01_081823 UTC
# URL: https://leetcode.com/submissions/detail/2089683719/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        iColor = image[sr][sc]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows = len(image)
        columns = len(image[0])
        def dfs(i, j):
            image[i][j] = color
            for r, c in directions:
                nr = i+r
                nc = j+c
                if -1<nr<rows and -1<nc<columns:
                    if image[nr][nc] == iColor:
                        dfs(nr, nc)
            return

        if color == iColor:
            return image
        dfs(sr, sc)
        return image

