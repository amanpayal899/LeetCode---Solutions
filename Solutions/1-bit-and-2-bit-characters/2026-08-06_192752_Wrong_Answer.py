# Problem: 1-bit and 2-bit Characters
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-06_192752 UTC
# URL: https://leetcode.com/submissions/detail/2097210177/

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)%2 == 0:
            return False
        return True