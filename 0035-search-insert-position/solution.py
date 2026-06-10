class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lb = n
        low = 0
        high = n-1
        while low <= high:
            mid = (high - low)//2 + low
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
