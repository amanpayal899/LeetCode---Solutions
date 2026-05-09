class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = -1
        missing = -1
        my_list = [0]*(n+1)
        for num in nums:
            my_list[num] += 1
        for i in range(1,n+1):
            if my_list[i] == 2:
                duplicate = i
            if my_list[i] == 0:
                missing = i
        return [duplicate, missing]

