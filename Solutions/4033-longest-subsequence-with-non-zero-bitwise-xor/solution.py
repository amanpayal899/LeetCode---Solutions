class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        all_zero = 1
        result = 0
        for i in nums:
            if i!=0:
                all_zero = 0
            result ^= i
        if result:
            return n
        if all_zero == 1:
            return 0
        return n-1

