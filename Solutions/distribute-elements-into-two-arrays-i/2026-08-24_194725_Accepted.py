# Problem: Distribute Elements Into Two Arrays I
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.2 MB
# Submitted: 2026-08-24_194725 UTC
# URL: https://leetcode.com/submissions/detail/2118918349/

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1= []
        arr2 = []
        arr1.append(nums[0])
        arr2.append(nums[1])
        for i in range(2, n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2
