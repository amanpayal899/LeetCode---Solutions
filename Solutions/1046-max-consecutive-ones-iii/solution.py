class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        maxi = 0
        zeroes = 0
        n = len(nums)

        while right < n:
            if nums[right] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            maxi = max(maxi, right-left+1)
            right += 1

        return maxi
