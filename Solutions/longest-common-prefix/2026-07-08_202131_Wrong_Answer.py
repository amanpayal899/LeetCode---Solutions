# Problem: Longest Common Prefix
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-08_202131 UTC
# URL: https://leetcode.com/submissions/detail/2061011156/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        n = len(strs)

        for i in range(len(strs[0])):
            for j in range(1,n):
                if i>=len(strs[j]):
                    break
                if strs[0][i] == strs[j][i]:
                    if j == n-1:
                        result += strs[0][i]
                else:
                    break
        return result
        
            
                 