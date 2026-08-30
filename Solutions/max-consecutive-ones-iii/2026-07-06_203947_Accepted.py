# Problem: Max Consecutive Ones III
# Status: Accepted
# Language: python3
# Runtime: 53 ms
# Memory: 22.3 MB
# Submitted: 2026-07-06_203947 UTC
# URL: https://leetcode.com/submissions/detail/2058535558/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        zeroes = 0
        maxi = 0
        my_queue = deque()
        while r<n:
            while  r < n and (nums[r] == 1 or zeroes < k):
                if nums[r] == 0:
                    my_queue.append(r)
                    zeroes += 1
                r += 1
            maxi = max(maxi, r-l)
            if my_queue:
                l = my_queue.popleft() + 1
                zeroes = k-1
            else:
                r += 1
                l = r
        return maxi