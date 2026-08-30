# Problem: Rearrange Array Elements by Sign
# Status: Accepted
# Language: python3
# Runtime: 75 ms
# Memory: 43 MB
# Submitted: 2026-06-04_214127 UTC
# URL: https://leetcode.com/submissions/detail/2022710140/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nArr = []
        pArr = []
        for i in nums:
            if i >= 0:
                pArr.append(i)
            else:
                nArr.append(i)
        i = len(nums)
        k=0
        for j in range(0, i):
            if j%2 == 0:
                nums[j] = pArr[k]
            else:
                nums[j] = nArr[k]
                k += 1
        return nums
