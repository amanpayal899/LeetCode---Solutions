# Problem: Smallest Missing Integer Greater Than Sequential Prefix Sum
# Status: Accepted
# Language: python3
# Runtime: 3 ms
# Memory: 19.2 MB
# Submitted: 2026-08-11_201714 UTC
# URL: https://leetcode.com/submissions/detail/2103412332/

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]+1
        largest = nums[0]
        sum = nums[0]
        for j in range(1, len(nums)):
            if nums[j]-1 == nums[j-1]:
                largest = nums[j]
                sum += nums[j]
            else:
                break
        missing = copy.copy(sum)
        while True:
            if missing not in nums:
                break
            else:
                missing += 1

        return missing
        
