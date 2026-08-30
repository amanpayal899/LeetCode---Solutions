# Problem: Flood Fill
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Submitted: 2026-07-30_160254 UTC
# URL: https://leetcode.com/submissions/detail/2087734508/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        r = len(image)
        c = len(image[0])
        startColor = image[sr][sc]
        image[sr][sc] = color
        queue = deque()
        queue.append((sr, sc))

        while queue:
            size = len(queue)
            while size>0:
                i, j = queue.popleft()
                if ( i>0 and image[i-1][j]==startColor ):
                    queue.append((i-1, j))
                    image[i-1][j] = color
                if ( i<r-1 and image[i+1][j]==startColor ):
                    queue.append((i+1, j))
                    image[i+1][j] = color
                if ( j>0 and image[i][j-1]==startColor ):
                    queue.append((i, j-1))
                    image[i][j-1] = color
                if ( j<c-1 and image[i][j+1]==startColor ):
                    queue.append((i, j+1))
                    image[i][j+1] = color
                size -= 1
            
        return image
                
