class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        n = len(nums)
        for i in range(0, n):
            conjugate = target - nums[i]
            if conjugate in hash_table:
                return [i, hash_table[conjugate]]
            hash_table[nums[i]] = i
        
