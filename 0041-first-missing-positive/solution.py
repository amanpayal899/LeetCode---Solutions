class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        for i in range(0,len(nums)):
            if ( nums[i]<=0 or nums[i]==nums[i-1] and i!=0 ):
                continue
            elif ( nums[i]!= count):
                return count
            count += 1
        return count



