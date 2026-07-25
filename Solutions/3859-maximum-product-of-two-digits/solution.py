class Solution:
    def maxProduct(self, n: int) -> int:
        def max(n):
            l1 = -1
            l2 = -1
            while n > 0:
                temp = n%10
                n = n//10
                if temp >= l1:
                    l2 = l1
                    l1 = temp
                elif temp > l2:
                    l2 = temp
            return l1*l2

        return max(n)
