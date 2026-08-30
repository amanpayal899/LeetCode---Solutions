# Problem: Max Consecutive Ones III
# Status: Accepted
# Language: python3
# Runtime: 59 ms
# Memory: 22.3 MB
# Submitted: 2026-07-07_070915 UTC
# URL: https://leetcode.com/submissions/detail/2058937861/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        maxi = 0
        zeroes = 0
        n = len(nums)

        while right < n:
            if nums[right] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            maxi = max(maxi, right-left+1)
            right += 1

        return maxi