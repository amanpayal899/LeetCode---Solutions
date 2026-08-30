# Problem: Exactly One Consecutive Set Bits Pair
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Submitted: 2026-06-17_202700 UTC
# URL: https://leetcode.com/submissions/detail/2036833882/

class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        count = 0
        prev = - 1
        current = -2
        while n != 0:
            prev = current
            current = n & 1
            if prev == current and current == 1:
                count += 1
            n >>= 1
        if count == 1:
            return True
        return False
                
            
        