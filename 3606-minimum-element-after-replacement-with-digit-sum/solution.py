
def digit_sum(num):
    if num//10 == 0:
        return num
    return num%10 + digit_sum(num//10)
class Solution:
    def minElement(self, nums: List[int]) -> int:
        length = len(nums)
        min = nums[0]
        for i in range(0, length):
            nums[i] = digit_sum(nums[i])
            if(nums[i] < min):
                min = nums[i]
        return min
