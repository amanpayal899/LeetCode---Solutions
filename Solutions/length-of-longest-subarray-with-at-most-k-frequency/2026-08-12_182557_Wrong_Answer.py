# Problem: Length of Longest Subarray With at Most K Frequency
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-12_182557 UTC
# URL: https://leetcode.com/submissions/detail/2104630104/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {}
        cpy = copy.copy(nums)
        c = 0
        tc = 0
        for i in range(len(cpy)):
            d[nums[i]] = d.get(nums[i], 0)+1
            if d[nums[i]] <= k:
                tc+=1
                if tc>=c:
                    c=tc
            else:
                tc = 1
            
        return c

                