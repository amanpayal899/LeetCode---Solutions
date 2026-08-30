# Problem: Find Missing Elements
# Status: Accepted
# Language: python3
# Runtime: 19 ms
# Memory: 19.2 MB
# Submitted: 2026-08-04_194457 UTC
# URL: https://leetcode.com/submissions/detail/2094549199/

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        min = nums[0]
        max = nums[0]
        l = len(nums)
        for i in nums:
            if i<min:
                min = i
            if i>max:
                max = i
        j = min
        while j<=max:
            i=0
            while i<l:
                if nums[i]==j:
                    break
                i+=1
            if i==l:
                result.append(j)
            j+=1

        return result

        
