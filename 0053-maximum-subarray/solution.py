class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = 0
        for i in nums:
            if sum + i > i:
                sum += i
                
            else:
                sum = i
            if sum > max_sum:
                max_sum = sum

        return max_sum
                
