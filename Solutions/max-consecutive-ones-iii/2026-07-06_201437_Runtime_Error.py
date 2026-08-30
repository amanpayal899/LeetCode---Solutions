# Problem: Max Consecutive Ones III
# Status: Runtime Error
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-06_201437 UTC
# URL: https://leetcode.com/submissions/detail/2058523623/

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
            l = my_queue.popleft() + 1
            zeroes = k-1
        return maxi