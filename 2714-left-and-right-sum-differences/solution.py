class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result_arr = [0]*n
        left_sum_arr = [0]*n
        right_sum_arr = [0]*n
        
        left_sum, right_sum = 0, 0
        for i in range(n):
            left_sum_arr[i] = left_sum
            left_sum += nums[i]
            right_sum_arr[n-i-1] = right_sum
            right_sum += nums[n-i-1]
        for i in range(n):
            result_arr[i] = abs(left_sum_arr[i] - right_sum_arr[i])
        return result_arr
        

