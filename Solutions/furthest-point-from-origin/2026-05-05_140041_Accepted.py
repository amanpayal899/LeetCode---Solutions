# Problem: Furthest Point From Origin
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19 MB
# Submitted: 2026-05-05_140041 UTC
# URL: https://leetcode.com/submissions/detail/1995857259/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        _count = 0
        right_count = 0
        left_count = 0
        for i in moves:
            if i == 'R':
                right_count += 1
            elif i == 'L':
                left_count += 1
            else:
                _count += 1
        if right_count > left_count:
            return right_count + _count - left_count
        return left_count + _count -right_count