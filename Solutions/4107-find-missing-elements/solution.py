class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        min = nums[0]
        max = nums[0]
        l = len(nums)
        for i in nums:
            if i<min:
                min = i
            if i>max:
                max = i
        j = min
        while j<=max:
            i=0
            while i<l:
                if nums[i]==j:
                    break
                i+=1
            if i==l:
                result.append(j)
            j+=1

        return result

        

