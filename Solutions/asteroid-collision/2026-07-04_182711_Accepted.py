# Problem: Asteroid Collision
# Status: Accepted
# Language: python3
# Runtime: 8 ms
# Memory: 20.3 MB
# Submitted: 2026-07-04_182711 UTC
# URL: https://leetcode.com/submissions/detail/2056154578/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                while stack and stack[-1] > 0 and abs(i) > stack[-1]:
                    stack.pop()
                if stack and abs(i) == stack[-1]:
                    stack.pop()
                elif not stack:
                    stack.append(i)
                elif stack[-1] < 0:
                    stack.append(i)
        return stack
