class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        l = len(nums)
        i=0
        while i<l-1 and ( nums[i]==nums[i+1]-1):
            i+=1
        prefixSum = sum(nums[:i+1])
        numsSet = set(nums)
        while prefixSum in numsSet:
            prefixSum += 1
        return prefixSum 
