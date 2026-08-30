# Problem: Add Binary
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB
# Submitted: 2026-04-08_174957 UTC
# URL: https://leetcode.com/submissions/detail/1972863162/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        carry = 0
        result = ""
        while( i>=0 or j>=0 or carry >0):
            if i>=0 and j>=0:
                ans = int(a[i])+int(b[j])+carry
                carry = 0
            elif i<0 and j<0 and carry>0:
                result += str(carry)
                break
            elif i<0:
                ans = int(b[j])+carry
                carry = 0
            elif j<0:
                ans = int(a[i])+carry
                carry = 0
            if ans==0 or ans==1:
                result += str(ans)
            if ans==2:
                result += "0"
                carry = 1
            if ans==3:
                result += "1"
                carry = 1
            i -= 1
            j -= 1
        result = result[::-1]
        return result