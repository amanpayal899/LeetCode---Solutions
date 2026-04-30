class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(0,32):
            rev <<= 1
            rev = rev | (n&1)
            n >>= 1
           
        return rev
