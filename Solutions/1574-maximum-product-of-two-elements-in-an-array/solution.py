class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstLarge = float('-inf')
        secondLarge = float('-inf')
        n = len(nums)
        for i in range(n):
            if nums[i]-1 >= firstLarge:
                secondLarge = firstLarge
                firstLarge = nums[i]-1
            elif nums[i]-1 > secondLarge:
                secondLarge = nums[i]-1
        return firstLarge*secondLarge
    

