class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        sum = 0
        x = 1
        while x <= k+n:
            if (abs(n - x) <= k) and (x & n == 0):
                sum += x
            x += 1
        return sum
