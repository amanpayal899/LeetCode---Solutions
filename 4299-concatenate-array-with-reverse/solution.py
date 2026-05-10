class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        length = len(nums)
        ans = nums + [0]*length
        for i in range(length):
            ans[length+i] = nums[length - i-1]
        return ans
        
