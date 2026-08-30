# Problem: 1-bit and 2-bit Characters
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-06_193703 UTC
# URL: https://leetcode.com/submissions/detail/2097217584/

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        return not (bits[len(bits)-2])