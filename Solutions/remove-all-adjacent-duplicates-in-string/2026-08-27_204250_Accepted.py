# Problem: Remove All Adjacent Duplicates In String
# Status: Accepted
# Language: python3
# Runtime: 35 ms
# Memory: 20.1 MB
# Submitted: 2026-08-27_204250 UTC
# URL: https://leetcode.com/submissions/detail/2122354079/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        stack = []
        
        #🤦‍♂️ sometimes it feels so  easy!!
        for i in  range(n):
            if len(stack)==0:
                stack.append(s[i])
            elif s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        result = ""
        for i in stack:
            result += i
        return result