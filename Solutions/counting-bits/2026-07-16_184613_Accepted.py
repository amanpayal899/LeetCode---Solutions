# Problem: Counting Bits
# Status: Accepted
# Language: python3
# Runtime: 35 ms
# Memory: 20.3 MB
# Submitted: 2026-07-16_184613 UTC
# URL: https://leetcode.com/submissions/detail/2070322388/

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for i in range(1, n+1):

            c = 0
            while i != 0:
                c+=1
                i = i&(i-1)
            result.append(c)
        return result