class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for i in range(1, n+1):

            c = 0
            while i != 0:
                c+=1
                i = i&(i-1)
            result.append(c)
        return result
