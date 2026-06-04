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
