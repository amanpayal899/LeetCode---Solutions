# Problem: Build an Array With Stack Operations
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Submitted: 2026-04-26_181213 UTC
# URL: https://leetcode.com/submissions/detail/1988853741/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        j=0
        for i in range (1,n+1):
            if i == target[j]:
                j+=1
                s.append("Push")
            else:
                s.append("Push")
                s.append("Pop")
            if j == len(target):
                break

        return s