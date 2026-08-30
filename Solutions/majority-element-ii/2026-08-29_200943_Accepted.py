# Problem: Majority Element II
# Status: Accepted
# Language: python3
# Runtime: 11 ms
# Memory: 23.7 MB
# Submitted: 2026-08-29_200943 UTC
# URL: https://leetcode.com/submissions/detail/2124320232/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[i] == (len(nums)//3)+1:
                result.append(i)
        return result
                