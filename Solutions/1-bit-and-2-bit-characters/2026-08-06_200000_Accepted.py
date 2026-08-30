# Problem: 1-bit and 2-bit Characters
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.5 MB
# Submitted: 2026-08-06_200000 UTC
# URL: https://leetcode.com/submissions/detail/2097234052/

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        c=0
        while c<len(bits)-1:
            if bits[c]==1:
                c+=1
            c+=1
        if c==len(bits):
            return False
        return True
        