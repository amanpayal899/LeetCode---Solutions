class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        k, j = 0, 1
        for i in range(0,n):
            if nums[i] >= 0:
                result[k] = nums[i]
                k += 2
            else:
                result[j] = nums[i]
                j += 2
        return result
