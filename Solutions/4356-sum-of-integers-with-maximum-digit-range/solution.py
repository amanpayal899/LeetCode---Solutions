class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        largest_range = 0
        arr = []
        n = len(nums)
        for i in range(n):
            
            temp = nums[i]
            maxi = 0
            min = nums[i]
            
            while temp != 0:
                if temp%10 < min:
                    min = temp%10
                if temp%10 > maxi:
                    maxi = temp%10
                temp //= 10
            arr.append(maxi-min)
            if maxi - min > largest_range:
                largest_range = maxi-min
                
        sum = 0
        for i in range(n):
            if arr[i] == largest_range:
                sum += nums[i]
            
        return sum
            
        
                
