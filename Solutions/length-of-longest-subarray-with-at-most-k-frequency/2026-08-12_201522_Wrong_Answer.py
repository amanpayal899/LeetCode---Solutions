# Problem: Length of Longest Subarray With at Most K Frequency
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-12_201522 UTC
# URL: https://leetcode.com/submissions/detail/2104728231/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {}
        cpy = copy.copy(nums)
        count = 0
        lenght = len(nums)
        l = 0
        r = 0
        while r<lenght:
            d[nums[r]] = d.get(nums[r], 0) +1
            if d[nums[r]] <= k:
                r+=1
                if r-l >= count:
                    count = r-l
            else:
                while d[nums[l]] != d[nums[r]]:
                    l+=1
                d[nums[l]] = d[nums[l]] -  1
                l+=1
                r+=1
        return count
            

                