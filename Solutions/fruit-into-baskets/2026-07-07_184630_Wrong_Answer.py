# Problem: Fruit Into Baskets
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-07_184630 UTC
# URL: https://leetcode.com/submissions/detail/2059707094/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        p1 = 0
        p2 = 0
        p3 = 0
        n = len(fruits)
        while p3 < n:
            while p2 < n-1 and fruits[p1] == fruits[p2]:
                p2 += 1
            p3 = p2 + 1
            
            while p3 < n and (fruits[p3] == fruits[p1] or fruits[p3] == fruits[p2]):
                p3 += 1
            max_fruits = max(max_fruits, p3-p1)
            p1 = p2
            p2 = p3

        return max_fruits


