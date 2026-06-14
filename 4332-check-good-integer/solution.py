class Solution:
    def digit(self, n):
        if n == 0:
            return
        last_digit = n%10
        self.digit_sum += last_digit
        self.square_sum += last_digit * last_digit
        self.digit(n//10)
        return
    def checkGoodInteger(self, n: int) -> bool:
        self.digit_sum = 0
        self.square_sum = 0
        self.digit(n)
        if self.square_sum - self.digit_sum >= 50:
            return True
        return False
        
