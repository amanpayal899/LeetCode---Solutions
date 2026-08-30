# Problem: Rearrange Array Elements by Sign
# Status: Accepted
# Language: python3
# Runtime: 42 ms
# Memory: 43.3 MB
# Submitted: 2026-06-05_201656 UTC
# URL: https://leetcode.com/submissions/detail/2023648821/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        k, j = 0, 1
        for i in range(0,n):
            if nums[i] >= 0:
                result[k] = nums[i]
                k += 2
            else:
                result[j] = nums[i]
                j += 2
        return result