# Problem: Add Strings
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-28_200501 UTC
# URL: https://leetcode.com/submissions/detail/2123269149/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = ""
        ptr1, ptr2 = len(num1)-1, len(num2)-1
        while ptr1>=0  and ptr2>=0:
            temp = int(num1[ptr1]) + int(num2[ptr2]) + carry
            if temp > 9:
                carry = temp//10
                temp = temp%10
                
            result = str(temp) + result
            ptr1-=1
            ptr2-=1
        while ptr1>=0:
            temp = int(num1[ptr1]) + carry
            result = str(temp) +  result
            carry = temp//10
            ptr1-=1
        while ptr2>=0:
            temp = int(num2[ptr2]) + carry
            result = str(temp) +  result
            carry = temp//10
            ptr2-=1
        return result
        

