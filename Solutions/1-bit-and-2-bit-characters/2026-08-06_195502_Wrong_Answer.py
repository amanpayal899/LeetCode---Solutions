# Problem: 1-bit and 2-bit Characters
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-06_195502 UTC
# URL: https://leetcode.com/submissions/detail/2097230789/

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        l = len(bits)
        if bits[l-2]==0 or (l%2 == 1):
            return True
        return False