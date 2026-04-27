class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        # Look at every second element (0, 2, 4...)
        for i in range(0, len(nums) - 1, 3):
            if nums[i] != nums[i + 1]:
                return nums[i]
        
        # If we reached the end, the last element must be the single one
        return nums[-1]
