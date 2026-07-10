class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        temp = copy.copy(n)
        while temp>0:
            c += 1
            temp = (((~temp)+1)^temp)&temp
        return c
