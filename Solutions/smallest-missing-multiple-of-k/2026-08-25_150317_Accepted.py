# Problem: Smallest Missing Multiple of K
# Status: Accepted
# Language: python3
# Runtime: 4 ms
# Memory: 19.4 MB
# Submitted: 2026-08-25_150317 UTC
# URL: https://leetcode.com/submissions/detail/2119788631/

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums2 = sorted(nums)
        smallest_multiple = k
        count = 1
        for i in nums2:
            if i == smallest_multiple:
                count += 1
                smallest_multiple = k * count
        return smallest_multiple

        
