# Problem: Best Time to Buy and Sell Stock
# Status: Accepted
# Language: python3
# Runtime: 35 ms
# Memory: 28.5 MB
# Submitted: 2026-06-04_165231 UTC
# URL: https://leetcode.com/submissions/detail/2022503703/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        min_price = prices[0]
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                max_p = max(max_p, i - min_price)

        return max_p