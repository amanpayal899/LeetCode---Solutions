# Problem: Destroying Asteroids
# Status: Accepted
# Language: python3
# Runtime: 76 ms
# Memory: 33.9 MB
# Submitted: 2026-05-31_182043 UTC
# URL: https://leetcode.com/submissions/detail/2018418064/

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in asteroids:
            if i > mass:
                return False
            mass += i
        return True
