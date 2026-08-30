# Problem: Smallest Missing Integer Greater Than Sequential Prefix Sum
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-11_200808 UTC
# URL: https://leetcode.com/submissions/detail/2103406568/

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]+1

        longestSeqCount = 0
        largestInSeq = 0
        longestSeqSum = 0
        currSeqSum = nums[0]
        currSeqCount = 1
        for i in range(1, len(nums)):
            if nums[i]-1 == nums[i-1]:
                currSeqCount += 1
                currSeqSum += nums[i]
                if currSeqCount >= longestSeqCount:
                    longestSeqCount = currSeqCount
                    longestSeqSum = currSeqSum
                    largestInSeq = nums[i]
            else:
                currSeqCount = 1
                currSeqSum = nums[i]

        
        missing = copy.copy(longestSeqSum)
        for i in range(50):
            if missing not in nums:
                return missing
            else:
                missing += 1


